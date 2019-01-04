'''
Created on Aug 21, 2018
@author: Prashant.Pal

'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import inplace
from _datetime import datetime

dfs = pd.read_html("https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2018")

row, column = dfs[1].shape
print('This are the rows = ' + repr(row) +' & columns ' + repr(column))

print(dfs[1][1:,])

df_main = pd.DataFrame()
df_main = dfs[1][1:,]
print(df_main)

#setting the index to one of the columns .. in this case column=0
df_main.set_index(df_main[0],inplace=True,drop=True)


df_main[0] = pd.to_datetime(df_main[0])
print(df_main.dtypes)

print(df_main)
ax=plt.gca()

print(df_main.loc['Date', 1:174])

df_main.plot(kind='Line',x=0,y=1,ax=ax)
plt.show()

df_main.plot()
# df_main=dfs[1]

# print(dfs[1][2:5])
# 
# print (dfs[1].columns)
# 
# print (dfs[1][0]) #Just printing Date Column ie 0
# 
# print (dfs[1][1][2:].min())

x = []
y = []

# for i in dfs[1].iteritems():
#     x.append(dfs[1][])
    

# def graph_data(x,y):
#     
#     ax = plt.gca()
#     plt.plot(kind='line',x=dfs[1][0],)
#     plt.xlabel(x)
#     plt.ylabel(y)
#     plt.title("Interesing quotes")
#     plt.legend()
#     plt.show()
#      
#      
# graph_data(dfs[1][0],range(10))    

# ax=plt.gca()
# 
# dfs[1].plot(kind='line',x=0,y=1,ax=ax)
# plt.show()

# for df in dfs:
#     print(df)


