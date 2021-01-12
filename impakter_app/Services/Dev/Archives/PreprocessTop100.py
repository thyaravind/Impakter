import pandas as pd
import streamlit as st
import sqlite3

companies_df = pd.read_csv("../../../../ProjectData/Top100BrandsData.csv")


'''
st.header("Before preprocessing")
st.write(companies_df)


df = pd.read_csv("../../../ProjectData/Top100BrandsData.csv",
                 usecols = ['Brand','Country','Brand Revenue','Stock Market ticker','Rating A-B-C-D-F'],
                 nrows = 20)

df.rename(columns = {'Brand':'Company','Brand Revenue': 'Revenue','Stock Market ticker':'Stock','Rating A-B-C-D-F':'Rating'},inplace = True)


df['stock_market'] = df.Stock.apply(lambda x: x.split(':')[0].strip())
df['ticker'] = df.Stock.apply(lambda x: x.split(':')[1].strip())
df['ID'] = df['stock_market'] + df['ticker']

st.write(df)

'''

sqlite_file = '/impakter_app/data.sqlite'
cnx = sqlite3.connect(sqlite_file)
c = cnx.cursor()

for company in companies_df.Brand:
    company
    c.execute("insert into companies_temp (name) values (?)", (str(company),))

cnx.commit()
cnx.close()