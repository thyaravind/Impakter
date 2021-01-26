from urllib.parse import urlparse
import sqlite3
import numpy as np
import pandas as pd
'''
article_url = "https://apple.com/2020/291210304284"

source_url = urlparse(article_url).netloc

if not source_url.startswith("www."):
    source_url = "www."+source_url

source = source_url[4:]
print(source_url)
print(source)
'''

sqlite_file = '/DB/data.sqlite'
cnx = sqlite3.connect(sqlite_file)
cursor = cnx.cursor()
sqlite3.register_adapter(np.int64, int)


sources = pd.read_sql('select sourceID,name,source_url from sources', cnx)
print(sources.columns)