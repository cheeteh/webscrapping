'''
Created on Aug 24, 2018

@author: Prashant.Pal
'''
import pandas as pd
import matplotlib.pyplot as plt
mylist=['A','B','C','D','E']
mydict = {'X':[1,2,3,4,5],'Y':[20,30,40,50,60],'Z':[50,60,70,80,90]}
mydict1 = {0:[1,2,3,4,5],1:[20,30,40,50,60],2:[50,60,70,80,90]}

#print(mylist[1:])

df = pd.DataFrame(mydict)
print(df)

df1 = pd.DataFrame(mydict1)
print(df1)


ax= plt.gca()

# df.plot(kind='Line',x='X',y='Y',ax=ax)
# df.plot(kind='Line',x='X',y='Z',ax=ax)

# plt.show()


df1.plot(kind='Line',x=0,y=1,ax=ax)
df1.plot(kind='Line',x=0,y=2,ax=ax)

plt.show()

# x = []
# y = []
# 
# x,y = [x,y for key,value in df.iteritems()]

# for i in dict_test:
#     x.append(i)
#     for j in dict_test[i].size():
#         y.append(dict_test[i])
#     
# print(x)
# print(y)

# plt.plot(x,y,linewidth=2.0)

