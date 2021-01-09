from bs4 import BeautifulSoup
import re
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import json
import pandas as pd
import requests



class CompanyProcessor:


    def __init__(self,company= 'na',wiki_url = 'na'):
        self.__company = company
        self.__wiki_url = wiki_url


    def wiki_data(self):

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




    def GetForbes2000(self):

        headers = {
            "accept": "application/json, text/plain, */*",
            "referer": "https://www.forbes.com/global2000/",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }

        cookies = {
            "notice_behavior": "expressed,eu",
            "notice_gdpr_prefs": "0,1,2:1a8b5228dd7ff0717196863a5d28ce6c",
        }

        api_url = "https://www.forbes.com/forbesapi/org/global2000/2020/position/true.json?limit=2000"
        response = requests.get(api_url, headers=headers, cookies=cookies).json()

        sample_table = [
            [
                item["organizationName"],
                item["country"],
                item["revenue"],
                item["profits"],
                item["assets"],
                item["marketValue"]
            ] for item in
            sorted(response["organizationList"]["organizationsLists"], key=lambda k: k["position"])
        ]

        df = pd.DataFrame(sample_table, columns=["Company", "Country", "Revenue", "Profits", "Assets", "Market Value"])
        df.to_csv(f"ProjectData/lists/forbes_2020.csv", index=False)


    def is_forbes_2000(self):

        data = pd.read_csv("app/Services/ProjectData/lists/forbes_2020.csv")
        data = data[data['Company'].str.match(self.__company)]

        return not data.empty


    def get_sic_code(self):
        data = pd.read_csv("app/Services/ProjectData/company_sic_database.csv")
        search_string = self.__company.upper()
        data = data[data['COMPANY'].str.upper().str.contains(search_string, regex=False)]
        data.drop(columns=['CIK'], inplace=True)
        return data


'''
    def process(self):
        wiki_status, wiki_output = self.wikiScraper(self)
        is_forbes_2000 = self.IsForbes2000(self)
        return wiki_status,wiki_output,is_forbes_2000

'''






