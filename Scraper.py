import requests
from RPA.Browser.Selenium import Selenium

# Define constants
TIMEOUT = 10
ScrapeItem = 2
POST_API_URL = "http://localhost:8000/visualize/api/item/"
GET_API_URL = "http://localhost:8000/visualize/scrape_data_list/"

XPATH = {
    "items": "//div[@class='gridItem--Yd0sa']//div[@class='info--ifj7U']//a",
    "name": "//span[@class='pdp-mod-product-badge-title']",
    "category": "//div[@id='pdp-nav']//ul//li[1]",
    "price": "//div[contains(@class,'pdp-product-price')]/span",
    "sold_by": "//div[@class='seller-name__detail']",
    "rating": "//span[@class='score-average']",
    "reviews": "//div[@class='mod-reviews']//div[@class='item']",
    "about": "//a[normalize-space()='About Daraz']",
}


class DarazScraper:
    """
    A class for scraping data from Daraz website.

    Args:
        category_url (str): The URL of the category to scrape.

    Attributes:
        browser (Selenium): A Selenium browser instance.
        category_url (str): The URL of the category being scraped.
    """

    def __init__(self, category_url: str | None = None):
        """
        Initializes a new DarazScraper instance.

        Args:
            category_url (str): The URL of the category to scrape.
        """
        self.browser = Selenium()
        self.category_url = category_url

    def open_browser(self):
        """
        Opens the web browser and maximizes it.

        Raises:
            Exception: If the browser is not found.
        """
        print("Opening Browser")
        self.browser.open_available_browser(url=self.category_url, maximized=True)
        print("Browser found")

    def is_daraz_link(self):
        """
        Checks if the provided URL is a valid Daraz link.

        Returns:
            bool: True if it's a valid Daraz link, False otherwise.
        """
        prefix = "https://www.daraz.com.np/"
        return self.category_url.startswith(prefix)

    def search_item(self):
        """
        Searches for items on the Daraz website.

        Returns:
            list: A list of item links.
        """
        item_data_list = []
        self.browser.wait_until_element_is_visible(XPATH["items"])
        items_elements = self.browser.find_elements(XPATH["items"])
        item_data_list = [
            items_element.get_attribute("href") for items_element in items_elements
        ]
        return item_data_list

    def collect_item_data(self, url):
        """
        Collects data for a specific item.

        Args:
            url (str): The URL of the item to collect data for.

        Returns:
            dict: A dictionary containing item data.
        """
        items_data = {}
        self.browser.go_to(url)
        temp_item = {}
        temp_item["vendor"] = "Daraz"
        try:
            self.browser.wait_until_element_is_visible(XPATH["about"])
            self.browser.scroll_element_into_view(XPATH["about"])
        except Exception as e:
            print(e)
        try:
            print("Get name")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["name"], timeout=TIMEOUT
            )
            temp_item["name"] = self.browser.find_element(XPATH["name"]).text
        except Exception as e:
            temp_item["name"] = "no name"
            print(e)
        try:
            print("Get category")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["category"], timeout=TIMEOUT
            )
            temp_item["category"] = self.browser.find_element(XPATH["category"]).text
        except Exception as e:
            temp_item["category"] = "no category"
            print(e)
        try:
            print("Get score")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["rating"], timeout=TIMEOUT
            )
            temp_item["rating"] = self.browser.find_element(XPATH["rating"]).text
        except Exception as e:
            temp_item["rating"] = 0
            print(e)
        try:
            print("Get price")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["price"], timeout=TIMEOUT
            )
            temp_item["price"] = self.browser.find_element(XPATH["price"]).text
        except Exception as e:
            temp_item["price"] = 0.0
            print(e)
        try:
            print("Get sold_by")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["sold_by"], timeout=TIMEOUT
            )
            temp_item["sold_by"] = self.browser.find_element(XPATH["sold_by"]).text
        except Exception as e:
            temp_item["sold_by"] = "no sold_by"
            print(e)
        try:
            print("Reviews")
            self.browser.wait_until_element_is_visible(
                locator=XPATH["reviews"], timeout=TIMEOUT
            )
            reviews_elements = self.browser.find_elements(XPATH["reviews"])
            reviews_list = [
                review.text
                for index, review in enumerate(reviews_elements)
                if index < 4
            ]
            print(reviews_list)

            # temp_item["reviews"] = ", ".join(reviews_list)
            temp_item["reviews"] = reviews_list
        except Exception as e:
            temp_item["reviews"] = "no reviews"
            print(e)

        print(f"temp item = {temp_item}")
        items_data = temp_item.copy()

        return items_data


class PostAPI:
    """
    A class for interacting with a POST API.

    Args:
        post_api_url (str): The URL of the POST API.
        get_api_url (str): The URL of the GET API for checking connectivity.
    """

    def __init__(self, post_api_url, get_api_url) -> None:
        """
        Initializes a new PostAPI instance.

        Args:
            post_api_url (str): The URL of the POST API.
            get_api_url (str): The URL of the GET API for checking connectivity.
        """
        self.post_api_url = post_api_url
        self.get_api_url = get_api_url

    def check_connection(self):
        """
        Checks the connectivity to the GET API.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        conn = requests.get(self.get_api_url)
        if conn.status_code == 200:
            return True
        return False

    def post_data(self, data_list):
        """
        Posts data to the POST API.

        Args:
            data_list (list): A list of data to be posted.

        Note:
            If any element in the data_list is None, it will not be posted.
        """
        for data in data_list:
            if data is None:
                break
            conn = requests.post(self.post_api_url, data=data)
            if conn.status_code == 201:
                print(f"Post Successful")
            else:
                print(f"Post unsuccessful")


if __name__ == "__main__":
    # Get the category URL from user input
    category_url = input("Enter category URL: ")

    # Create instances of DarazScraper and PostAPI
    daraz_scraper = DarazScraper(category_url)
    api = PostAPI(POST_API_URL, GET_API_URL)

    # Check if the provided URL is a valid Daraz link
    if not daraz_scraper.is_daraz_link():
        raise Exception("Invalid URL")

    # Open the web browser
    daraz_scraper.open_browser()

    # Search for items on the Daraz website
    items_links = daraz_scraper.search_item()
    print(f"Number of items found: {len(items_links)}")
    print(f"Example item link: {items_links[0]}")

    # Collect item data for up to 10 items
    data_list = [
        daraz_scraper.collect_item_data(url=url) if (index < ScrapeItem) else None
        for index, url in enumerate(items_links)
    ]
    print("All data collected")

    # Check the connection to the API
    print("Checking connection to the API")
    if api.check_connection():
        print("Connection successful")
    else:
        print("Connection failed")

    # Post collected data to the API
    print("Posting data to the API")
    api.post_data(data_list)
    print("Data Posted")

    # Close the web browser
    daraz_scraper.browser.close_browser()
