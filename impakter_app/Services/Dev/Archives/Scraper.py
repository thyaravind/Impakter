from bs4 import BeautifulSoup
import re
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import json
import sqlite3
import datetime
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('chromedriver')

cnx = sqlite3.connect(':memory')

class NewsScraper:


    def reutersScraper(self):
        def scrap(topic):

            driver.get(f'https://www.reuters.com/news/archive/{topic}news?view=page&page=2&pageSize=10')

            count = 0
            headlines = []
            dates = []
            links = []
            news_links = []
            for x in range(3):
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
                        print(headline.text)
                        news_links.append(headline.find_element_by_xpath('..').get_attribute('href'))
                    for date in news_dates:
                        dates.append(date.text)
                        print(date.text)
                        count = count + 1
                        print("CLICKED!!:")
                except Exception as e:
                    print(e)
                    break
            articles_dictionary = {}
            articles_dictionary = dict(zip(headlines, news_links))
            with open(f'../ProjectData/news_sources/reuters_{topic}.json', 'w') as f:
                json.dump(articles_dictionary, f)

        topics = ['business','esg','technology','world','environment']
        for topic in topics:
            scrap(topic)


    def ecowatchScraper(self):

        driver.get('https://ecotopical.com/ecowatch/')

        count = 0
        headlines = []
        dates = []
        links = []
        news_links = []
        for x in range(1):
            try:
                # loadMoreButton.click()
                # time.sleep(3)
                # loadMoreButton = driver.find_element_by_class_name("widget__headline-text")
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                # time.sleep(3)
                # loadMoreButton.click()
                time.sleep(2)
                news_headlines = driver.find_elements_by_class_name("go")
                # news_dates = driver.find_elements_by_class_name("timestamp")
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
        articles_dictionary = dict(zip(headlines, news_links))
        with open('../../data/scrapingData/news_sources/ecowatch_sustainability.json', 'w') as f:
            json.dump(articles_dictionary, f)



    def datesplitter(self,df):
        df['year'] = df.date.map(lambda x: x.year)
        df['month'] = df.date.map(lambda x: x.month)
        df['date'] = df.date.map(lambda x: x.date)
        df.drop(columns=['date'], inplace=True)
        return df



    def NewsScraper(load_more_button, news_headlines, news_dates,source_name,topic_name,source_link,date_format):
        driver.get(source_link)
        headlines = []
        dates = []
        news_links = []

        try:
            driver.get(source_link)
        except Exception as e:
            status = f"Error {e} occurred when connecting to the {source_name} website using driver"

        else:

            try:
                for x in range(2):
                    load_more_button.click()
                    time.sleep(2)
                    for headline in news_headlines:
                        headlines.append(headline.text)
                        news_links.append(headline.find_element_by_xpath('..').get_attribute('href'))
                    for date_element in news_dates:
                        date_extracted = datetime.datetime.strptime(date_element.text,date_format)
                        dates.append(date_extracted)
            except Exception as e:
                status = f"Error {e} occurred when scraping the {source_name}"
            else:
                df = pd.DataFrame(list(zip(headlines, news_links, dates)), columns=['headline', 'link', 'dates'])
                df['source'] = source_name
                df['topic'] = topic_name
                df['year'] = df.dates.map(lambda x: x.year)
                df['month'] = df.dates.map(lambda x: x.month)
                df.to_csv(f"{source_name}_{topic_name}.csv")
                status = f"successfully retrieved from {source_name}"
        return status



status = NewsScraper()