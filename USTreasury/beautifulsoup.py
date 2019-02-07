# @author: Prashant.Pal
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt


url_2018='https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2018'
url_2019='https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2019'

  
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
headers = {'User-Agent': user_agent}
response_2018_html = requests.get(url_2018,headers=headers).text
response_2019_html = requests.get(url_2019,headers=headers).text

soup_2018=BeautifulSoup(response_2018_html,'lxml')
soup_2019=BeautifulSoup(response_2019_html,'lxml')

table_data_2018 = soup_2018.find_all('table')[1]
table_data_2019 = soup_2019.find_all('table')[1]
# print(table_data_2019.prettify())

df_2018=pd.read_html(str(table_data_2018))[0]
df_2019=pd.read_html(str(table_data_2019))[0]

df_final=df_2018.append(df_2019.iloc[1:],ignore_index=True)

df_final.columns=df_final.iloc[0]
df_final = df_final.iloc[1:]
df_final.index = pd.to_datetime(df_final.iloc[0:,0])
print(df_final)

df_final['30 yr'].astype(float).plot(kind='line',legend=True)
df_final['10 yr'].astype(float).plot(kind='line',legend=True)
df_final['5 yr'].astype(float).plot(kind='line',legend=True)
df_final['1 mo'].astype(float).plot(kind='line',legend=True)
df_final['6 mo'].astype(float).plot(kind='line',legend=True)
 
plt.show()
