'''
Created on Dec 18, 2018

@author: Prashant.Pal
'''
import matplotlib.pyplot as plt


x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

population_ages = [22,34,56,78,80,24,34,1,1,5,6,17,15,23,45,12]

#ids = [x for x in range(len(population_ages))]

# ------------- Regular Graph -----------
#plt.plot(x,y, label='First line')
#plt.plot(x2,y2, label='Second line')

# ------------ Bar -------------
#plt.bar(x,y,label='Bar1',color='blue')
#plt.bar(x2,y2,label='Bar2',color='orange')

#plt.bar(ids, population_ages)

# ---------- Histogram - basically plotting in bins ------
# bins = [0,10,20,30,40,50,60,70,80,90,100]
# plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

# -------------- Scatter Plot ------------
#plt.scatter(x,y,label='skitscat',color='k' , marker='*', s=500)
# s for size in above line

# ---------------- Stack Plots --------------

days = [1,2,3,4,5]
 
sleeping = [7,8,5,11,6,]
eating = [2,1,2,3,4]
working = [8,9,6,7,5]
playing = [8,3,10,5,6]
# 
# plt.plot([],[],color='r',label='sleeping', linewidth=5)
# plt.plot([],[],color='b',label='eating', linewidth=5 )
# plt.plot([],[],color='g',label='working' , linewidth=5)
# plt.plot([],[],color='k',label='playing' , linewidth=5)
# 
# plt.stackplot(days,sleeping,eating,working,playing, colors=['r','b','g','k'])

# ------ Pie Charts ------------

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['m','c','r','g']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'
        )

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting graph')
plt.legend()
plt.show()
