import requests
from contextlib import closing
import csv
import pandas as pd

stock_list  = open("stock_list.txt", 'r') 

df = pd.DataFrame(index=[
	'2015-01-01',
	'2015-02-01',
	'2015-03-01',
	'2015-04-01',
	'2015-05-01',
	'2015-06-01',
	'2015-07-01',
	'2015-08-01',
	'2015-09-01',
	'2015-10-01',
	'2015-11-01',
	'2015-12-01',
	'2016-01-01',
	'2016-02-01',
	'2016-03-01',
	'2016-04-01',
	'2016-05-01',
	'2016-06-01',
	'2016-07-01',
	'2016-08-01',
	'2016-09-01',
	'2016-10-01',
	'2016-11-01',
	'2016-12-01',
	'2017-01-01',
	'2017-02-01',
	'2017-03-01',
	'2017-04-01',
	'2017-05-01',
	'2017-06-01',
	'2017-07-01',
	'2017-08-01',
	'2017-09-01',
	'2017-10-01',
	'2017-11-01',
	'2017-12-01',
	'2018-01-01',
	'2018-02-01',
	'2018-03-01',
	'2018-04-01',
	'2018-05-01',
	'2018-06-01',
	'2018-07-01',
	'2018-08-01',
	'2018-09-01',
	'2018-10-01',
	'2018-11-01',
	'2018-12-01',
	'2019-01-01',
	'2019-02-01',
	'2019-03-01',
	'2019-04-01',
	'2019-05-01',
	'2019-06-01',
	'2019-07-01',
	'2019-08-01',
	'2019-09-01',
	'2019-10-01',
	'2019-11-01',
	'2019-12-01',])

print(df)

for stock in stock_list:
	print (stock.strip())

	url = "https://query1.finance.yahoo.com/v7/finance/download/"+stock.strip()+".NS?period1=1419984000&period2=1577750400&interval=1mo&events=history"
	print(url)

	df[stock.strip()] = ""


	with closing(requests.get(url, stream=True)) as r:
	    f = (line.decode('utf-8') for line in r.iter_lines())
	    reader = csv.reader(f, delimiter=',', quotechar='"')
	    next(reader)
	    for row in reader:
	        # print(row[0])
	        df.at[row[0].strip(),stock.strip()] = row[5]
	print(df)

df.to_csv('stock_returns.csv')

stock_list.close()
