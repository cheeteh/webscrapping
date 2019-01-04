'''
Created on Dec 19, 2018

@author: Prashant.Pal
'''
import numpy as np
import matplotlib.pyplot as plt
from _struct import unpack

#Part1 
'''
import csv

x= []
y= []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from File')
'''

x,y = np.loadtxt('example.txt',delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from File')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting graph')
plt.legend()
plt.show()