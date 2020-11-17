import mysql.connector
from mysql.connector import errorcode


try:
    connection  = mysql.connector.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'aravind',
        password = 'impakter',
        database = 'impakter_index',
    )
    rev = 20
    print('connected successfully')
    cursor = connection.cursor()
    sql_query = ("insert into companies"
                 "(Company_ID,Company,Revenue,Country,Stock_market,Ticker,Company_Url,Outlook,Analyst_notes)"
                 "values(%(id)s,%(company)s,%(revenue)s,%(country)s,%(stock_market)s,%(ticker)s,%(company_url)s,%(outlook)s,%(notes)s)")
    info = {
        'id': 'COMP3',
        'company': 'company_name',
        'revenue': rev,
        'country': 'USA',
        'stock_market':'NYSE',
        'ticker': 'AAPLE',
        'company_url':'url',
        'outlook':'Positive',
        'notes':'texttttttt'

    }
    cursor.execute(sql_query, info)
    connection.commit()
    print('data updated')
    connection.close()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


