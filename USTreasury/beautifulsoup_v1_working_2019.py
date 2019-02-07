# @author: Prashant.Pal
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import matplotlib.pyplot as plt


# url='https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2019'
#  
 
# user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
# headers = {'User-Agent': user_agent}
# response_2019_html = requests.get(url,headers=headers).text
# 
# with open("treasury2019.html","w+") as file1:
#     file1.write(str(response_2019_html))

with open("treasury2019.html","r") as file1:
    response_2019=file1.read()
    

soup_2019=BeautifulSoup(response_2019,'lxml')

table_data_2019 = soup_2019.find_all('table')[1]
# print(table_data_2019.prettify())

df_2019=pd.read_html(str(table_data_2019))[0]
df_2019.columns=df_2019.iloc[0]

# print(df_2019.iloc[0:,0])
df_2019=df_2019.iloc[1:,0:]
df_2019.index=pd.to_datetime(df_2019.iloc[0:,0])

print(df_2019)

# df_2019.iloc[1:,1].astype(float).plot(x=pd.to_datetime(df_2019.iloc[1:,0]),legend=True)
df_2019['1 mo'].astype(float).plot(legend=True)
df_2019['10 yr'].astype(float).plot(legend=True)
df_2019['30 yr'].astype(float).plot(legend=True)

# with open("treasury2018.html","ra+") as file2:
#     response_2018=file2.read()
#     
#     
# # print(response)
# 
# 
# soup = BeautifulSoup(response_2018,'lxml') 
# # print(soup.prettify())
# table_data = soup.find_all('table')[1]
# # print(table_data.prettify())
# # print(len(list(table_data)))
# 
# df=pd.read_html(str(table_data))[0]
# # print(df)
# 
# df_desired=df.iloc[1:,1:].astype(float)
# # print(df.iloc[1:,0])
# 
# df_desired.columns=df.iloc[0,1:]
# df_desired.index=pd.to_datetime(df.iloc[1:,0])
# print(df_desired)
# 
# # print(df_desired)
# # df = pd.DataFrame(table_data)
# # print(df.head(5))
# ax = plt.gca()
# # df_desired.plot(ax=ax)
# df_desired['30 yr'].plot(kind='line',legend=True)
# df_desired['10 yr'].plot(kind='line',legend=True)
# 
plt.show()
