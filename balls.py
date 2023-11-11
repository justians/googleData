from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

dict = {}
counter = 0
options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('headless')
#global driver
driver = webdriver.Chrome(options=options)

def search():
    global driver
    try: 
        url= f'https://www.google.com/search?q={line}'
        driver.set_window_size(100,100)
        driver.get(url)
        page = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(page, "html.parser")
        combien = soup.find("div", {"id":"result-stats"}).text
        combien = int(combien[6:-24].translate({ord(','):None}))
        dict.update({line: combien})
        global counter 
        counter += 1
        print(f"Pages scanned: {counter}. . .")
    except:
        driver.quit()
        driver = webdriver.Chrome(options=options)
        
with open(r'C:\Users\iansp\Downloads\words.txt', 'r') as f:
# Do something with the file
    lines = f.readlines()

for line in lines:
    search()
    

print(dict)
driver.quit()
