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

source_link = 'https://www.reuters.com/news/archive/esgnews?view=page&page=2&pageSize=10'
number_of_pages = 2


def scrap(source_link,number_of_pages):

    driver.get(source_link)

    count = 0
    headlines =[]
    dates = []
    news_links = []

    for x in range(number_of_pages):
        try:
            # loadMoreButton.click()
            # time.sleep(3)
            loadMoreButton = driver.find_element_by_class_name("control-nav-next")
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            loadMoreButton.click()
            time.sleep(2)
            news_headlines = driver.find_elements_by_class_name("story-title")
            news_dates = driver.find_elements_by_class_name("timestamp")
            for headline in news_headlines:
                headlines.append(headline.text)

                news_links.append(headline.find_element_by_xpath('..').get_attribute('href'))
            for date in news_dates:
                dates.append(date.text)

                count=count+1

        except Exception as e:
            print(e)
            break
    dictt = {}
    dictt = dict(zip(headlines, news_links))
    return(dictt)