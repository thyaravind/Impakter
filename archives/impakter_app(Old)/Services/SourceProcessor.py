import pandas as pd
import requests
from bs4 import BeautifulSoup

class SourceProcessor:

    def __init__(self, source='na', source_url='na'):
        self.__source = source
        self.__source_url = source_url

    def get_wiki_data(self):
        """

        :return:
        """
        try:
            response = requests.get(self.__source_url)
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