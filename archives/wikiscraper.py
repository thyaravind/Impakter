from bs4 import BeautifulSoup
import re
import requests



url = 'https://en.wikipedia.org/wiki/Amazon_(company)'
try:
    response = requests.get(url)
    print(response.status_code)
except:
    print('Error occured while getting the web page')
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    wiki_sidebox = soup.find('table','infobox vcard')

    website_line = wiki_sidebox.find('th', string='Website')
    website_block = website_line.find_parent('tr')
    company_url = website_block.find('a').get('href')

    stock_ticker = wiki_sidebox.find(title='Ticker symbol').find_parent('tr').find('li').text
    revenue = wiki_sidebox.find(string='Revenue').find_parent('tr').find('td').text
    employees = wiki_sidebox.find(string='Number of employees').find_parent('tr').find('td').text

print(f"company_url:{company_url},\n employees: {employees},\n revenue: {revenue},\n stock_ticker: {stock_ticker},\n employees: {employees}")