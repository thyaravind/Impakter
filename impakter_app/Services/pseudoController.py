import News
import pandas as pd



'''
company = CompanyProcessor.CompanyProcessor(company="Apple", wiki_url=request.form['url'])
is_forbes_2000 = company.IsForbes2000
status, wiki_data = company.WikiData()
'''


'''
news = News.News()
df2 = news.google(start_date='05/01/2020',end_date='05/10/2020',keyword='Apple')
'''

# %% Testing the News object
'''
company = "Apple"

news = News.News()
print(f"processing the company {company}...")
news.google(start_date='01/01/2017', end_date='01/31/2017', company=company, keyword='Sustainability')
'''


# %% Data for top 100 brands - 2017 to 2020 - Sustainability


companies_df = pd.read_csv("/Users/aravind/OneDrive/OneDocuments/Algorithm/Impakter/ProjectData/Top100BrandsData.csv")

for company in companies_df.Brand[20:25]:
    news = News.News(start_date='01/01/2017', end_date='12/31/2020', company=company, keyword="Sustainability")
    print(f"processing the company {company}...")
    news.fetch_articles()

# completed from 15 to 20
# %%