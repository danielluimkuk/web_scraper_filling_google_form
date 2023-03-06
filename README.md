# Web Scraping Rental Property Information with Python
This project is a web scraper that extracts information about rental properties from Zillow and submits the data to a Google Form. It uses the Python programming language and the following libraries: requests, BeautifulSoup, and Selenium.

# Getting Started
Clone the repository to your local machine.
Install the required libraries by running pip install -r requirements.txt in your command line.
In the code, replace the driver_path variable with the path to your local Chrome driver.

Replace the GOOGLE_FORM_URL variable with the URL of your Google Form.
Run the code with python main.py.
How It Works
The web scraper sends a GET request to the Zillow rental search page and receives the HTML content in response. It then uses BeautifulSoup to extract the address, link, and price information for each rental property on the page. The information is stored in Python lists.

The scraper then uses Selenium to automate the submission of the data to the Google Form. For each rental property, it opens the form in a new Chrome window, fills in the address, price, and link fields, and submits the form.

## Acknowledgements

 - 100 days of Python by Angela Yu
