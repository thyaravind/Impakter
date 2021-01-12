from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import json
import pandas as pd
import requests


class CompanyProcessor:
    """
    Processes Company, fetches data from various resources

    """
    def __init__(self, company='na', wiki_url='na'):
        self.__company = company
        self.__wiki_url = wiki_url

    def get_wiki_data(self):
        """

        :return:
        """
        try:
            response = requests.get(self.__wiki_url)
            print(response.status_code)
        except:
            status = 'Error occured while getting the wiki page'
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            wiki_sidebox = soup.find('table', 'infobox vcard')

            website_line = wiki_sidebox.find('th', string='Website')
            website_block = website_line.find_parent('tr')
            company_url = website_block.find('a').get('href')

            stock_ticker = wiki_sidebox.find(title='Ticker symbol').find_parent('tr').find('li').text
            revenue = wiki_sidebox.find(string='Revenue').find_parent('tr').find('td').text
            employees = wiki_sidebox.find(string='Number of employees').find_parent('tr').find('td').text
            output = {}
            status = "fetched ProjectData successfully from Wikipedia"
            output['company_url'] = company_url
            output['stock_ticker'] = stock_ticker
            output['revenue'] = revenue
            output['employees'] = employees

        return status, output

    def is_forbes_2000(self):
        """
        Checks if a company is in Forbes 2000 list

        :return:
        """
        data = pd.read_csv("app/Services/ProjectData/lists/forbes_2020.csv")
        data = data[data['Company'].str.match(self.__company)]

        return not data.empty

    def get_sic_code(self):
        """
        Returns the probable list SIC codes for a given company

        :return:
        """
        data = pd.read_csv("app/Services/ProjectData/company_sic_database.csv")
        search_string = self.__company.upper()
        data = data[data['COMPANY'].str.upper().str.contains(search_string, regex=False)]
        data.drop(columns=['CIK'], inplace=True)
        return data

    def process(self):
        """
        Processes a newly added company
        :return:
        """
        wiki_status, wiki_output = self.wikiScraper(self)
        is_forbes_2000 = self.IsForbes2000(self)
        return wiki_status, wiki_output, is_forbes_2000
