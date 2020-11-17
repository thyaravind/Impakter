import pandas as pd
import streamlit as st

companies_df = pd.read_csv("data/Index.csv",
                           nrows = 20)
st.header("Before preprocessing")
st.write(companies_df)


df = pd.read_csv("data/Index.csv",
                           usecols = ['Brand','Country','Brand Revenue','Stock Market ticker','Rating A-B-C-D-F'],
                           nrows = 20)

df.rename(columns = {'Brand':'Company','Brand Revenue': 'Revenue','Stock Market ticker':'Stock','Rating A-B-C-D-F':'Rating'},inplace = True)


df['stock_market'] = df.Stock.apply(lambda x: x.split(':')[0].strip())
df['ticker'] = df.Stock.apply(lambda x: x.split(':')[1].strip())
df['ID'] = df['stock_market'] + df['ticker']

st.write(df)

