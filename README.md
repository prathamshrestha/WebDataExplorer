
# Web Data Explorer

 A web scraping system and a web portal to display the scraped data. 


## Authors

- [@prathamshrestha](https://github.com/prathamshrestha)


## API Reference

#### Post item

```http
  POST /api/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | AutoField | **Required**. Id of item  |
| `name`      | `string` |  Name og the product |
| `vendor`      | `string` |  Name of the vendor of the product |
| `category`      | `string` |  Category of the product |
| `rating`      | `decimal` |  Rating of the product |
| `price`      | `string` |  Price of the product |
| `reviews`      | `string` |  Reviews of the product |
| `sold_by`      | `string` |  Sold by information |



## Documentation

**1. Introduction** 
The Web Scraper is a Python script designed to extract product information from the website currently only for Daraz. It utilizes web scraping techniques to gather data such as product names, categories, prices, ratings, and more. And it posts to an API in django server and then displays into the webapp developed by django server.

**2. Dependencies**

RPA.Browser.Selenium: This module provides functionalities for browser automation using Selenium.

Django : This framework is used to create APIs and webapp.

Requests: This library is used for making HTTP requests to interact with APIs.

**3. Project Overview**
This project comprises a web application for displaying scraped data and an API for posting the scraped data, all built using the Django framework.

**4. System Description**
- Web Application: The web application, accessible at webexplorer, serves as the interface for viewing the scraped data. When the Django server is running, this [link](http://localhost:8000/visualize/scrape_data_list/) opens automatically.
- Streamlined Data Posting: An added feature of this project is the streamlined data posting process. Instead of inserting data directly into the database, it is sent directly to the Django server. This data can then be seamlessly displayed within the application. 
This approach simplifies data management, providing a more efficient and straightforward way to share and explore scraped data within the project.


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