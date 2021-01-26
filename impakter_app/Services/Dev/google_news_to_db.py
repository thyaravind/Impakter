from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import numpy as np
import datetime
from newspaper import Config
import nltk
import sqlite3
from simhash import Simhash

# establishing database connection
sqlite_file = '/DB/data.sqlite'
cnx = sqlite3.connect(sqlite_file)
c = cnx.cursor()
sqlite3.register_adapter(np.int64, int)

# fetching all sources first (into a df), categories
sources = pd.read_sql('select sourceID,name from sources', cnx)
categories = pd.read_sql('select categoryID,name from category_types', cnx)
companies = pd.read_sql('select companyID,name from companies_temp', cnx)

# initiating google news and config

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10

# doing google news search
company = "Intel"
keyword = "Sustainability"

news = GoogleNews(start='05/01/2020', end='05/31/2020')
news.search(company + " company " + keyword)

i = 0

try:
    for page_num in range(1, 2):
        news.getpage(page_num)
        result = news.result()
        df = pd.DataFrame(result)
        df.drop(columns=['img', 'desc', 'date'], inplace=True)
        df.rename(columns={'media': 'source', 'link': 'url'}, inplace=True)

        article_df = pd.DataFrame(
            columns=['id', 'url', 'source_id', 'content_hash', 'summary', 'category_id', 'company_id'])

        for ind in df.index:

            previous_articles = pd.read_sql('select articleID,sourceID from articles', cnx)
            article_id = str(Simhash(df['url'][ind]).value)
            source = df['source'][ind]

            if source == '':
                source = "Unknown"

            if source not in set(sources.name):
                source = str(source)
                c.execute("insert into sources (name) values (?)", (source,))
                cnx.commit()
                sources = pd.read_sql('select sourceID,name from sources', cnx)

            if article_id in set(previous_articles.articleID) or article_id in set(article_df.id):
                break
            else:
                article = Article(df['url'][ind], config=config)
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                except:
                    print(f"timed out when downloading {df['source'][ind]}")
                else:
                    article_df.at[i, 'id'] = article_id
                    article_df.at[i, 'url'] = df['url'][ind]
                    article_df.at[i, 'datetime'] = str(df['datetime'][ind])
                    article_df.at[i, 'source_id'] = np.int64(sources.loc[sources['name'] == source].reset_index().at[
                                                                 0, 'sourceID'])
                    article_df.at[i, 'summary'] = str(article.summary)
                    article_df.at[i, 'content_hash'] = str(Simhash(article.text).value)
                    article_df.at[i, 'category_id'] = np.int64(
                        categories.loc[categories['name'] == keyword].reset_index().at[
                            0, 'categoryID'])
                    article_df.at[i, 'company_id'] = np.int64(
                        companies.loc[companies['name'] == company].reset_index().at[
                            0, 'companyID'])
                    i += 1

    article_df.to_csv("articles.csv", index=False)
    article_df.to_sql(name='df4', con=cnx, if_exists='append')

    for ind in article_df.index:
        c.execute("insert into articles (articleID,url,sourceID,content_hash,summary,datetime) values (?,?,?,?,?,?)", (
            article_df.at[ind, 'id'], article_df.at[ind, 'url'], article_df.at[ind, 'source_id'],
            article_df.at[ind, 'content_hash'],
            article_df.at[ind, 'summary'], article_df.at[ind, 'datetime']))

        c.execute("insert into article_category (articleID,categoryID) values (?,?)",
                  (article_df.at[ind, 'id'], article_df.at[ind, 'category_id']))

        c.execute("insert into article_company (articleID,companyID) values (?,?)",
                  (article_df.at[ind, 'id'], article_df.at[ind, 'company_id']))



except Exception as e:
    print(f"Unable to perform action due to Error:{e}")
finally:
    cnx.commit()
    cnx.close()

