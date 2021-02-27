import pandas as pd
import numpy as np
import sqlite3
from urllib.parse import urlparse

# Adding url to existing sources

# establishing database connection
sqlite_file = '/impakter_app/data.sqlite'
cnx = sqlite3.connect(sqlite_file)
c = cnx.cursor()
sqlite3.register_adapter(np.int64, int)

sources = pd.read_sql('select sourceID,name from sources', cnx)

for _, source in sources.iterrows():
    print(source)
    try:
        c.execute("select url from articles where sourceID = ?", (source.sourceID,))
        article_url = c.fetchone()[0]
    except:
        print(f"failed updating the source {source.name}")
    else:
        source_url = urlparse(article_url).netloc
        c.execute("update sources set url = ? where sourceID = ?", (source_url, source.sourceID))
        print(source_url)

cnx.commit()
cnx.close()