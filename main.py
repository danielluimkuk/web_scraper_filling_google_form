import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time


headers = {
    'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36 '
}
url = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122' \
      '.66610182714844%2C%22east%22%3A-122.20055617285156%2C%22south%22%3A37.51922033645422%2C%22north%22%3A38' \
      '.03047869381536%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A' \
      '%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp' \
      '%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C' \
      '%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22' \
      '%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D '

GOOGLE_FORM_URL = 'https://forms.gle/yi3Kd7HyWtVW55Ub9'

# using selenium driver
driver_path = '/Users/DanielLui/Downloads/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(service=Service(driver_path))
driver.get(url)
time.sleep(5)

html_content = driver.page_source

# using requests
# response = requests.get(url, headers=headers)
# html_content = response.content

# making soup
soup = BeautifulSoup(html_content, 'html.parser')


addresses = []
links = []
prices = []

address_css = soup.select('li.ListItem-c11n-8-85-1__sc-10e22w8-0.srp__sc-wtsrtn-0.jhnswL.with_constellation a address')

for address in address_css:
    addresses.append(address.get_text().split('|')[-1])

link_css = soup.select('.StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0.jVBMsP.property-card-data a')
baseurl = 'https://www.zillow.com/'

for link in link_css:
    if 'http' not in link['href']:
        links.append(baseurl+link['href'])
    else:
        links.append(link['href'])

price_css = soup.select('.StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0.jVBMsP.property-card-data span')

for price in price_css:
    if '/' in price.get_text().split('+')[0]:
        prices.append(price.get_text().split('+')[0].split('/')[0])
    else:
        prices.append(price.get_text().split('+')[0])

# would be useful if there is more search result next page next_page_button = driver.find_element(By.CSS_SELECTOR,
# 'li.PaginationJumpItem-c11n-8-85-1__sc-18wdg2l-0 > a[rel="next"]') next_page_button.click()

# input("Press enter to close the browser window.")

for n in range(len(links)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div['
                                            '2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div['
                                          '2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                         '1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div['
                                                  '1]/div/span/span')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit_button.click()

