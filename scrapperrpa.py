import time
import requests
from typer import Typer
from selenium import webdriver
from selenium.webdriver.common.by import By
from RPA.Browser.Selenium import Selenium

app = Typer()
TIMEOUT = 10
XPATH = {
    'items':"//div[@class='gridItem--Yd0sa']//div[@class='info--ifj7U']//a",
    'name':"//span[@class='pdp-mod-product-badge-title']",
    'category':"//div[@id='pdp-nav']//ul//li[1]",
    'price':"//div[contains(@class,'pdp-product-price')]/span",
    'sold_by':"//div[@class='seller-name__detail']",
    'rating':"//span[@class='score-average']",
    'reviews':"//div[@class='mod-reviews']//div[@class='item']",
    'about':"//a[normalize-space()='About Daraz']"
}
API_URL = 'http://localhost:8000/visualize/create/'

class DarazScrapper:

    def __init__(self, category_url:str|None = None):
        self.browser = Selenium()  
        self.category_url = category_url

    def open_browser(self):
        print('Opening Browser')
        self.browser.open_available_browser(url=self.category_url, maximized=True)
        print('Browser found')

    def is_daraz_link(self):
        prefix = "https://www.daraz.com.np/"
        return self.category_url.startswith(prefix)

    def search_item(self):
        item_data_list = []
        self.browser.wait_until_element_is_visible(XPATH['items'])
        items_elements = self.browser.find_elements(XPATH['items'])
        item_data_list = [items_element.get_attribute('href') for items_element in items_elements]
        return item_data_list

    def collect_item_data(self, url):
        items_data = {}
        self.browser.go_to(url)
        temp_item = {}
        try:
            self.browser.wait_until_element_is_visible(XPATH['about'])
            self.browser.scroll_element_into_view(XPATH['about'])
        except Exception as e:
            print(e)
        try:
            print('Get name')
            self.browser.wait_until_element_is_visible(locator=XPATH['name'], timeout=TIMEOUT)
            temp_item['name'] = self.browser.find_element(XPATH['name']).text
        except Exception as e:
            temp_item['name'] = 'no name'
            print(e)
        try:
            print('Get category')
            self.browser.wait_until_element_is_visible(locator=XPATH['category'], timeout=TIMEOUT)
            temp_item['category'] = self.browser.find_element(XPATH['category']).text
        except Exception as e:
            temp_item['category'] = 'no category'
            print(e)
        try:
            print('Get score')
            self.browser.wait_until_element_is_visible(locator=XPATH['rating'], timeout=TIMEOUT)
            temp_item['rating'] = self.browser.find_element(XPATH['rating']).text
        except Exception as e:
            temp_item['rating'] = 0
            print(e)
        try:
            print('Get price')
            self.browser.wait_until_element_is_visible(locator=XPATH['price'], timeout=TIMEOUT)
            temp_item['price'] = self.browser.find_element(XPATH['price']).text
        except Exception as e:
            temp_item['price'] = 0.0
            print(e)
        try:
            print('Get sold_by')
            self.browser.wait_until_element_is_visible(locator=XPATH['sold_by'], timeout=TIMEOUT)
            temp_item['sold_by'] = self.browser.find_element(XPATH['sold_by']).text
        except Exception as e:
            temp_item['sold_by'] = 'no sold_by'
            print(e)
        try:
            print('Reviews')
            self.browser.wait_until_element_is_visible(locator=XPATH['reviews'], timeout=TIMEOUT)
            reviews_elements = self.browser.find_elements(XPATH['reviews'])
            reviews_list = [review.text for index, review in enumerate(reviews_elements) if index < 4]
            print(reviews_list)
            temp_item['reviews'] = ', '.join(reviews_list)
        except Exception as e:
            temp_item['reviews'] = 'no reviews'
            print(e)

        print(f'temp item = {temp_item}')
        items_data = temp_item.copy()

        return items_data
    
class PostAPI:
    def __init__(self, api_url) -> None:
        self.api_url = api_url

    def check_connection(self):
        conn = requests.get(self.api_url)
        if conn == 200:
            return True
        return False
    
    def post_data(self, datalist):
        for data in datalist:
            if data is None:
                break
            conn = requests.post(self.api_url, data=data)
            if conn.status_code == 200:
                print(f'Post Successful')
            else:
                print(f'Post unsuccessful')

if __name__ == '__main__':
    category_url = input('Enter category url: ')
    browser = DarazScrapper(category_url)
    api = PostAPI(API_URL)
    if not browser.is_daraz_link():
        raise Exception('Invalid url')
    
    browser.open_browser()

    items_links = browser.search_item()
    print(f'Length of items is {len(items_links)}')
    print(f'Few data of items links : {items_links[0]}')

    data_list = [browser.collect_item_data(url=url) if (index < 10) else None for index, url in enumerate(items_links)]
    print('All data collected')

    print('Checking connection')
    if api.check_connection():
        print('connection succesfull')
    else:
        print('connection failed')

    print('Posting data')
    api.post_data(data_list)
    print('Data Posted')

    browser.browser.close_browser()
