from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import json
import sqlite3
import datetime
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())


def news_scrap(source_link, next_button,next_type, news_headline, news_date, date_type, link_type, source_name, topic_name, date_format):

    headlines = []
    dates = []
    news_links = []

    try:
        driver.get(source_link)
    except Exception as e:
        status_message = f"Error {e} occurred when connecting to the {source_name} website using driver"
    else:

        try:
            for x in range(2):

                if next_type == 'xpath':
                    load_more_button = driver.find_element_by_xpath(next_button)
                elif next_type == 'class':
                    load_more_button = driver.find_element_by_class_name(next_button)
                load_more_button.click()
                time.sleep(2)
                news_headlines = driver.find_elements_by_class_name(news_headline)
                news_dates = driver.find_elements_by_class_name(news_date)
                for headline in news_headlines:
                    headlines.append(headline.text)

                    if link_type == 'xpath':
                        news_links.append(headline.find_element_by_xpath('..').get_attribute('href'))
                    elif link_type == 'tag':
                        news_links.append(headline.find_element_by_tag_name('a').get_attribute('href'))
                for date_element in news_dates:
                    if date_type == 'normal':
                        date_extracted = datetime.datetime.strptime(date_element.text.title(), date_format)
                        dates.append(date_extracted)
                    elif date_type == 'bulk':
                        date_extracted = datetime.datetime.strptime(date_element.text.title(), date_format)
                        dates.append(date_extracted)

        except Exception as e:
            status_message = f"Error {e} occurred when scraping the {source_name}"
        else:
            df = pd.DataFrame(list(zip(headlines, news_links, dates)), columns=['headline', 'link', 'dates'])
            df['source'] = source_name
            df['topic'] = topic_name
            df['year'] = df.dates.map(lambda x: x.year)
            df['month'] = df.dates.map(lambda x: x.month)
            df.to_csv(f"ProjectData/{source_name}_{topic_name}.csv")
            status_message = f"successfully retrieved from {source_name}"

    return status_message


#Reuters
"""
status_message = news_scrap(source_link='https://www.reuters.com/news/archive/esgnews?view=page&page=2&pageSize=10',
                            next_button="control-nav-next",
                            next_type= "class",
                            news_headline="story-title",
                            news_date="timestamp",
                            link_type='xpath',
                            date_type = 'normal',
                            source_name="Reuters",
                            topic_name="esg",
                            date_format='%b %d %Y')
"""

#GreenBiz
'''
status_message = news_scrap(source_link="https://www.greenbiz.com/collections/sustainability?page=1",
                            next_button="//a[@title='Go to next page']",
                            next_type= "xpath",
                            news_headline="article-teaser-vertical__title",
                            news_date="article-teaser-vertical__date",
                            link_type='tag',
                            date_type = 'normal',
                            source_name="GreenBiz",
                            topic_name="esg",
                            date_format='%B %d, %Y')
'''


#Financial Times --todo not working on FT
status_message = news_scrap(source_link="https://www.ft.com/companies?page=2",
                            next_button="//a[@ProjectData-trackable='next-page']",
                            next_type= "xpath",
                            news_headline="article-teaser-vertical__title",
                            link_type='tag',
                            news_date="o-date o-teaser__timestamp",
                            date_type='bulk',
                            source_name="Financial Times",
                            topic_name="business",
                            date_format='%B %d %Y')

#HBR

#
