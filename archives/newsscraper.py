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
import pandas as pd
import datetime
import sqlalchemy as db
import sqlite3

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome('chromedriver')
driver.get('https://www.reuters.com/news/archive/esgnews?view=page&page=2&pageSize=10')
import json
import pickle

engine = db.create_engine('sqlite:///news_articles.db', echo=True)
sqlite_connection = engine.connect()
metadata = db.MetaData()
df = db.Table('df', metadata, autoload=True, autoload_with=engine)

query = db.select([df])

count = 0
headlines =[]
dates = []
news_links = []

for x in range(2):
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
        for date_text in news_dates:
            date = datetime.datetime.strptime(date_text.text,'%b %d %Y')
            dates.append(date)

            count=count+1

    except Exception as e:
        print(e)
        break

df = pd.DataFrame(list(zip(headlines, news_links,dates)),columns=['headline','link','dates'])
df['source'] = 'Reuters'
df['topic'] = 'esg'
df['year'] = df.dates.map(lambda x: x.year)
df['month'] = df.dates.map(lambda x: x.month)

#todo resolve date not working

df.dates



df.to_sql("df", sqlite_connection, if_exists='append')


cnx = sqlite3.connect(':memory')
df.to_sql(name='df',con=cnx,if_exists='append')

#df2 = pd.read_sql('select * from df where month == "12"',cnx,parse_dates=True)



df.info()
