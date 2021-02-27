from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dateutil.parser
import time
import csv
from datetime import datetime
import io
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome('chromedriver')
driver.get('https://ecotopical.com/ecowatch/')
import json
import pickle


count = 0
headlines =[]
dates = []
links = []
news_links = []
for x in range(1):
    try:
        # loadMoreButton.click()
        # time.sleep(3)
        #loadMoreButton = driver.find_element_by_class_name("widget__headline-text")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #time.sleep(3)
        #loadMoreButton.click()
        time.sleep(2)
        news_headlines = driver.find_elements_by_class_name("go")
        #news_dates = driver.find_elements_by_class_name("timestamp")
        for headline in news_headlines:
            headlines.append(headline.text)
            print(headline.text)
            news_links.append(headline.get_attribute('href'))
        """for date in news_dates:
            dates.append(date.text)
            print(date.text)
            count=count+1
            print("CLICKED!!:")"""
    except Exception as e:
        print(e)
        break
dictt = {}
dictt = dict(zip(headlines, news_links))
with open('../../data/scrapingData/news_sources/ecowatch_sustainability.json', 'w') as f:
    json.dump(dictt,f)

print(headlines)