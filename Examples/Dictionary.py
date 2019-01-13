#defining dictionary
import matplotlib.pyplot as plt
from test.test_asyncore import bind_af_aware


my_dict = {'1MO': { '2019-01-01':2.4, 
                    '2019-01-02':2.5,
                    '2019-01-03':2.7,
                    '2019-01-04':2.1
                   },
           '2MO': { '2019-01-01':3.4,
                    '2019-01-02':3.5,
                    '2019-01-03':3.7,
                    '2019-01-04':3.1
                   }       
          }

bond_time_list=[]
for i in my_dict:
    bond_time_list.append(i)
    

dates_per_bond_time_list=[]
interest_per_bond_time_list=[]

for bond_time,data_per_bond_time_dict in my_dict.items():
    
    #initiated two separate list for getting the nested dict data in form of a list
    dates_list=[]
    interest_value_list=[]
    for dates,interest_value in data_per_bond_time_dict.items():
        dates_list.append(dates)
        interest_value_list.append(interest_value)
    
    #adding the two list created per key of the nested dict to separate list for plot    
    dates_per_bond_time_list.append(dates_list)
    interest_per_bond_time_list.append(interest_value_list)
    
    
print(dates_per_bond_time_list)
print(interest_per_bond_time_list)   

    
plt.plot(dates_per_bond_time_list[0],interest_per_bond_time_list[0], label ="1 MO")    
plt.plot(dates_per_bond_time_list[1],interest_per_bond_time_list[1], label ="2 MO")
plt.xlabel("Dates")
plt.ylabel("Interest Rates")
plt.legend()
plt.show() 

# -- Prints each Value 
# print(my_dict.values())

# -- Prints just keys
# print(my_dict.keys())

# -- Iterate through each item
# for bond_time,data_per_bond_time_dict in my_dict.items()
#     print(bond_time,data_per_bond_time_dict) 

