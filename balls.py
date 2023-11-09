from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
driver = webdriver.Chrome()
url = "https://www.google.com/search?p=trees"
driver.maximize_window()
driver.get(url)

page = driver.page_source.encode('utf-8').strip()

soup = BeautifulSoup(page, 'html.parser')

combien = soup.find('div', {'id': 'result-stats'}).text

print(int(combien[6:-24].translate({ord(','): None})))

driver.quit()
