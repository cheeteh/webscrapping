# @author: Prashant.Pal

import bs4 as bs
import requests
import pandas as pd
import re

#first get the URL & get a response from the site
url='https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2018'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)

#create a soup & find that table
soup = bs.BeautifulSoup(response.content,'html5lib') 
table_data = soup.find_all('table')[1]
# print(table_data)

#create data-frame from that html piece for table above
df = pd.read_html(str(table_data))[0]
df.columns=df.loc[0]




