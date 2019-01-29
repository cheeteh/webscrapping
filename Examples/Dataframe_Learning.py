'''
Created on Jan 14, 2019

@author: Prashant.Pal
'''


import pandas as pd
import numpy as np


df =pd.DataFrame(
                 [['2019-01-01',1,2,3],['2019-01-02',2,3,4],['2019-01-03',12,22,32],['2019-01-04',14,25,36]],
                 index = [0,1,2,3],
                 columns=['Date','1 MO','2 MO','3 MO']
                )
# filename="dataframe_example_created.txt"
# df = pd.read_csv(filename)

# tfile=open('dataframe_example_created.txt','a')
# tfile.write(df.to_string())
# tfile.close()

# print(df.head(2))
# print(df.tail(2))

# print(df.dtypes) #Prints type of all the fields
# print(df.index)  #RangeIndex(start=0, stop=4, step=1)
# print(df.columns)# Prints all the columns\
print (len(df)) #print total number of rows in dataframe
# print(df.values) #gives all values in list
# print(df.describe()) #gives mean, std, min, max, 25%, 50%, 75%
# print(df.sort_values('3 MO',ascending=False)) #Descending data by one field


# print(df['Date']) #Print a column data
# print(df.Date) #Print a column data
# print(df[0:1]) #Print rows 2 to 4
# print(df.loc[0:1,['Date','1 MO']]) #Print rows and columns
# print(df[['1 MO','2 MO']]) #Print particular columns
# print(df.loc[3,['Date','1 MO']]) # Prints that row and the particular column specified
# print(df.iloc[0:1,[2,3]]) #Print particular rows and  particular column but using the index
# df_desired=df.iloc[1:len(df),1:12].astype(float) #select columns collectively like rows and convert all to float
# print(df[df['2 MO'] > 5]) #Print all the rows where 2 MO is greater than 5
# print(df[df['3 MO'].isin([32])]) #Print all rows where 3 MO is in 32

# df.loc[0,['1 MO']]=100 #Assigning or changing the value of Dataframe
# df.loc[1,['2 MO']]=np.nan
# print(df.iloc[0,[1]]) #gives you the 1st line basically + 2nd column 
# print(df.iloc[0]) #gives you the 1st line basically
# print(df.loc[0]) #gives you the 1st line basically
# print(df.loc[1,['2 MO']])
# df.loc[:,['3 MO']]= np.array([5] * len(df)) #Assign values to one particular column
# df['total']=(df['1 MO'] + df['2 MO'] + df['3 MO'])/3 #Create another column with averaging values from other columns

# df.rename(columns={'2 MO':'4 MO'},inplace=True) # Rename a particular column
# df.columns = ['DATED','1 MO','2 MO','3 MO'] # Rename the columns name in bulk
# print(df)
# 
# for index,x in df.iterrows():
#     print(index,x['1 MO'],x['2 MO'],x['3 MO'])
#     
# df.to_csv('dataframe_example_csv')







