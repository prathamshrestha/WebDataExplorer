
# Web Data Explorer

 A web scraping system and a web portal to display the scraped data. 


## Authors

- [@prathamshrestha](https://github.com/prathamshrestha)


## API Reference

#### Post Product item

```http
  POST http://localhost:8000/visualize/api/create
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | AutoField | **Required** Id of item  |
| `name`      | `string` |  Name of the product |
| `vendor`      | `string` |  Name of the vendor of the product |
| `category`      | `string` |  Category of the product |
| `rating`      | `decimal` |  Rating of the product |
| `price`      | `string` |  Price of the product |
| `reviews`      | `string` |  Reviews of the product |
| `sold_by`      | `string` |  Sold by information |



## Documentation

**1. Introduction** 
The Web Scraper is a Python script designed to extract product information from the website currently only for Daraz. It utilizes web scraping techniques to gather data such as product names, categories, prices, ratings, and more. And it posts the scrapped data item to the API server, this api server is developed using Django framework. 

I used Selenium for web scraping tasks that require interacting with dynamic web pages, handling JavaScript, and mimicking user interactions like clicking buttons or scrolling. It provides a high level of control and flexibility.

In this project, Django serves two primary purposes:

Web Application: Django is used to create the web application that displays the scraped data. It handles routing, views, and templates, allowing you to present the scraped data in a user-friendly format.

API Development: Django is also used to develop the API endpoints. APIs are crucial for communication between different components of the system, enabling the seamless transfer of data from the web scraping process to the web application.

The scrapper and the visualization server communicate together through API requests. 

**2. Dependencies**

RPA.Browser.Selenium: This module provides functionalities for browser automation using Selenium.

Django : This framework is used to create APIs and webapp.


**3. Project Overview**
This project comprises a web application for displaying scraped data and an API for posting the scraped data, all built using the Django framework.

**4. System Description**
- Web Application: The web application, accessible at webexplorer, serves as the interface for viewing the scraped data. When the Django server is running, this browsable [link](http://localhost:8000/scrape_data_list/) opens the page to visulaize all the scraped data.
- Streamlined Data Posting: An added feature of this project is the streamlined data posting process. Instead of inserting data directly into the database, it is sent directly to the Django server. This data can then be seamlessly displayed within the application. 
- This approach simplifies data management, providing a more efficient and straightforward way to share and explore scraped data within the project. 
- 

## Installation

- Install Python 3.x

```bash
  git clone https://github.com/the-username/daraz-scraper.git
```
Change into the project directory:
```bash
  cd WEBDATAEXPLORER
```
Create a virtual environment:
```bash
  pip install venv
  source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  pip install -r requirements.txt
```
Start the Django Server.
```bash
  cd webdataexplorer
  python manage.py runserver
```
With the Django project's server running, you can now run the scraper script:
```bash
  cd ..
  python daraz_scraper.py
``` 


## Additional Notes

#### 1. If your system is relatively simple, please also describe how the "perfect" version of your system would look. What additional features or improvements would you add?

This system currently can handle only the category link from daraz and is relatively simple. We can add several features like 
- add several other vendors like sastodeal, sajilohop, neostore, okdam and so on and apply factory design pattern with multithreading.
- Market analysis of the product.

#### 2. Describe how you would implement a notification system into this project. What tools or frameworks would you use? How would it function?

There are several ways to implement Notifications like
- Email: Python libraries like smtplib and Django's built-in email support to send email notifications.
- Messaging Services: Services like Twilio or Pusher can be used to send SMS or push notifications.
Also Django provides a built-in mechanism called "signals" that allows decoupled applications to get notified when certain actions occur elsewhere in the application. You can use signals to trigger notifications when specific events happen in your project.

However, I was planning to implement the email system in the following ways:
1. Build a Email component using smtplib and a queue system where we can put following logs:
- When scraping is successful, emit a "scraping_successful" signal.
- When an error occurs during scraping, emit a "scraping_error" signal.
- When data is posted successfully to the API, emit a "data_posted" signal.
2. Then we put these logs into the queue then export it into excel or csv.
3. Then we send it to the reciepents.


#### 3. Consider scalability: If this system was expected to handle a billion records a month, how would you change the design? What architectural decisions would you make to ensure smooth operation at this scale?

Handling a billion records a month is a significant scalability challenge that requires careful architectural decisions and optimizations. To ensure smooth operation at this scale, consider the following architectural decisions and changes to the design:
- Database Optimization: Use a highly scalable and distributed database system like postgresql  that can handle large volumes of data.
- Implement data partitioning and sharding strategies to distribute data across multiple database nodes.
- Data Ingestion: Implement a robust data ingestion pipeline that can handle high data volumes efficiently. Consider using tools like Apache Kafka or RabbitMQ for real-time data ingestion. Use batch processing techniques (e.g., Apache Spark) for processing large datasets.
- Caching: Implement caching mechanisms to reduce the load on the database. Use in-memory caching solutions like Redis to store frequently accessed data. Employ content delivery networks (CDNs) to cache and serve static content (e.g., images, CSS, JavaScript) to reduce server load.
- Load Balancing: Employ load balancers to distribute incoming traffic across multiple application server instances. Use auto-scaling to dynamically adjust the number of application server instances based on traffic demand.
- Indtroduce microservice architecture to Decompose the application into microservices that can scale independently. Each microservice can handle specific functions (e.g., scraping, data storage, API) and can be scaled horizontally as needed.
