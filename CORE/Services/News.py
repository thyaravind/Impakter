import sys
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import datetime
from newspaper import Config
import nltk
import sqlite3
import numpy as np
from simhash import Simhash
from urllib.parse import urlparse


# nltk.download('punkt')


class News:
    """
    News Object retrieves news articles from various resources and adds them to the database
    """

    @staticmethod
    def initialize_db_and_config():
        """
        Initializing database connection and configuration settings

        :return:
        """
        # configuration
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent
        config.request_timeout = 10

        # establishing database connection
        sqlite_file = '/Users/aravind/OneDrive/OneDocuments/Algorithm/Impakter/DB/data.sqlite'
        cnx = sqlite3.connect(sqlite_file)
        cursor = cnx.cursor()
        sqlite3.register_adapter(np.int64, int)
        return cnx, cursor, config

    def close_db_connection(self):
        """
        Closes Db connection
        """
        self.cnx.commit()
        self.cnx.close()

    def __init__(self):
        self.cnx, self.cursor, self.config = self.initialize_db_and_config()
        self.start_date = None
        self.__end_date = datetime.datetime.now()
        self.__period = None
        self.__company = None
        self.__keyword = 'General'
        self.__search_string = None
        self.__num_of_pages = None
        self.__categories = pd.read_sql('select categoryID,name from category_types', self.cnx)
        self.__companies = pd.read_sql('select companyID,name from companies_temp', self.cnx)
        self.__sources = pd.read_sql('select sourceID,name,source_url from sources', self.cnx)

    def fetch(self, start_date='', end_date=datetime.datetime.now(), company='', keyword='General', num_of_results=500,
              period=''):
        """
        Sequence of methods when articles are to be fetched
        """
        self.__sources = pd.read_sql('select sourceID,name,source_url from sources', self.cnx)
        self.start_date = start_date
        self.__end_date = end_date
        self.__period = period
        self.__company = company
        self.__keyword = keyword
        self.__search_string = company + " company " + keyword
        self.__num_of_pages = int(num_of_results / 10)

        articles = self.google()
        if not articles.empty:
            articles_analysed = self.process_articles(articles)
            if not articles_analysed.empty:
                self.commit_to_db(articles_analysed)
            else:
                print(f"No new articles for the company {self.__company}")
        else:
            print(f"No articles retrieved for the given criteria of the company {self.__company}")

    def google(self):
        """
        Fetches articles from Google News page
        :return: returns a dataframe with article details
        """
        print(f"fetching articles from Google for {self.__company}")
        if self.__period == '':
            news = GoogleNews(start=self.start_date, end=self.__end_date)
        else:
            news = GoogleNews(period=self.__period)

        news.search(self.__search_string)
        try:
            # Fetch articles
            for page_num in range(1, self.__num_of_pages):
                print(f"Fetching articles from page: {page_num}")
                news.getpage(page_num)
                result = news.result()
                df = pd.DataFrame(result)
                df.drop(columns=['img', 'desc', 'date'], inplace=True)
                df.rename(columns={'media': 'source', 'link': 'url'}, inplace=True)
        except Exception as e:
            print(f"Unable to fetch articles from google due to Error:{e}")  # todo logger
            sys.exit(f"Unable to fetch articles from google due to Error:{e}")
        else:
            print(f"Completed fetching articles from Google for {self.__company}")
            return df

    def bing(self):
        """
        Fetching articles using bing
        """
        pass

    def process_source(self, article_url):
        """
        processes each source

        :param source:
        :param article_url:
        """
        source_url = urlparse(article_url).netloc
        if not source_url.startswith("www."):
            source_url = "www." + source_url
        source = source_url[4:]
        if source_url not in set(self.__sources.source_url):
            source = str(source)
            self.cursor.execute("insert into sources (name,source_url) values (?,?)", (source, source_url))
            self.cnx.commit()
            self.__sources = pd.read_sql('select sourceID,name,source_url from sources', self.cnx)
        return source, source_url

    def process_articles(self, raw_article_df):
        """
        Performs NLP tasks on each article and creates a dataframe
        :param raw_article_df:
        :return:
        """
        print(f"processing articles for {self.__company}")
        i = 0
        article_df = pd.DataFrame(
            columns=['id', 'url', 'source_id', 'content_hash', 'summary', 'content', 'keywords',
                     'category_id',
                     'company_id'])
        previous_articles = pd.read_sql('select articleID,sourceID from articles', self.cnx)

        for ind in raw_article_df.index:
            print(f"processing article:{ind}")
            article_id = str(Simhash(raw_article_df['url'][ind]).value)
            article_url = raw_article_df['url'][ind]
            source, source_url = self.process_source(article_url)

            if article_id in set(previous_articles.articleID) or article_id in set(article_df.id):
                continue
            else:
                article = Article(raw_article_df['url'][ind], config=self.config)
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                except Exception as e:
                    print(
                        f"timed out when downloading {raw_article_df['source'][ind]} with the following error: {e}")
                else:
                    article_df.at[i, 'id'] = article_id
                    article_df.at[i, 'url'] = raw_article_df['url'][ind]
                    article_df.at[i, 'datetime'] = str(raw_article_df['datetime'][ind])
                    article_df.at[i, 'source_id'] = np.int64(
                        self.__sources.loc[self.__sources['source_url'] == source_url].reset_index().at[
                            0, 'sourceID'])
                    article_df.at[i, 'summary'] = str(article.summary)
                    article_df.at[i, 'keywords'] = str(article.keywords)
                    article_df.at[i, 'content'] = str(article.text)
                    article_df.at[i, 'content_hash'] = str(Simhash(article.text).value)
                    article_df.at[i, 'category_id'] = np.int64(
                        self.__categories.loc[self.__categories['name'] == self.__keyword].reset_index().at[
                            0, 'categoryID'])
                    article_df.at[i, 'company_id'] = np.int64(
                        self.__companies.loc[self.__companies['name'] == self.__company].reset_index().at[
                            0, 'companyID'])
                    i += 1
        print(f"Completed processing articles for {self.__company}")
        return article_df

    def commit_to_db(self, article_df):
        """
        Commits all the new articles to the database
        :param article_df:
        """
        print(f"Adding articles for {self.__company} to the database")
        # article_df.to_sql(name='articles_duplicate_2', con=cnx, if_exists='append')
        try:
            for ind in article_df.index:
                self.cursor.execute(
                    "insert into articles (articleID,url,sourceID,content_hash,summary,content,keywords,datetime) values (?,?,?,?,?,?,?,?)",
                    (
                        article_df.at[ind, 'id'], article_df.at[ind, 'url'], article_df.at[ind, 'source_id'],
                        article_df.at[ind, 'content_hash'],
                        article_df.at[ind, 'summary'], article_df.at[ind, 'content'], article_df.at[ind, 'keywords'],
                        article_df.at[ind, 'datetime']))

                self.cursor.execute("insert into article_category (articleID,categoryID) values (?,?)",
                                    (article_df.at[ind, 'id'], article_df.at[ind, 'category_id']))

                self.cursor.execute("insert into article_company (articleID,companyID) values (?,?)",
                                    (article_df.at[ind, 'id'], article_df.at[ind, 'company_id']))
            print(f"Added articles for {self.__company} to the database")
        except Exception as sql_error:
            print(f"error occurred during sql commit with error {sql_error}")  # todo logs
