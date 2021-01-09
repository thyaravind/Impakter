from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import datetime
from newspaper import Config
import nltk
import sqlite3
from simhash import Simhash

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10



googlenews=GoogleNews(start='05/01/2020',end='05/31/2020')
googlenews.search('Cocacola')


for i in range(1,4):
    googlenews.getpage(i)
    result=googlenews.result()
    df=pd.DataFrame(result)
    df.drop(columns=['img','desc','date'],inplace=True)
    df.rename(columns={'media':'source','link':'url'},inplace=True)
    df['article'] = ''
    df['summary'] = ''

    for ind in df.index:
        article = Article(df['url'][ind], config=config)
        try:
            article.download()
            article.parse()
            article.nlp()
            df.loc[ind,'contentHash'] = Simhash(article.text).value

            df.loc[ind,'summary'] = article.summary
        except:
            print(f"timed out when downloading {df['source'][ind]}")


df.to_csv("articles.csv")


cnx = sqlite3.connect('/impakter_app/ProjectData.sqlite')
df.to_sql(name='df2',con=cnx,if_exists='append')