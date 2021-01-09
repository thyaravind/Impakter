import sqlite3
import sqlalchemy as db
import pandas as pd

df = []

'''
#option 1
cnx = sqlite3.connect(':memory')
df.to_sql(name='df',con=cnx)

p2 = pd.read_sql('select * from df', cnx)
'''


'''
#option 2
engine = db.create_engine('sqlite:///save_pandas.db', echo=True)
sqlite_connection = engine.connect()
metadata = db.MetaData()
df = db.Table('df', metadata, autoload=True, autoload_with=engine)


df.to_sql("df", sqlite_connection, if_exists='fail')

count = db.select([db.func.count([df])])


sqlite_connection.close()

'''


#%% Performing operations

sqlite_file = r'/impakter_app/ProjectData.sqlite'
cnx = sqlite3.connect(sqlite_file)
c = cnx.cursor()


#%% dataframe operations
df.to_sql(name='df',con=cnx)

#%%
sources = pd.read_sql('select sourceID,name from sources', cnx)


#%% Normal querying
c.execute(f'SELECT * from sources')

all_rows = c.fetchall()

source = str("source name")
c.execute("insert into sources (name) values (?)",(source,))


cnx.commit()
cnx.close()


#%% article operation

df = pd.read_csv("/impakter_app/Services/ProjectData/articles.csv")

for ind in df.index:
    c.execute("insert into articles (articleID,url,sourceID,content_hash,summary) values (?,?,?,?,?)", (str(df.loc[ind, 'id']), df.loc[ind, 'url'], df.loc[ind, 'source_id'], str(df.loc[ind, 'content_hash']), df.loc[ind, 'summary']))

cnx.commit()
cnx.close()