# @author: Prashant.Pal

import bs4 as bs
from urllib.request import Request, urlopen
import urllib.parse
import pandas as pd
import re

'''
sauce = urllib.request.urlopen("https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2018").read()
soup = bs.BeautifulSoup(sauce,'html5lib')

tables = soup.find('table', attrs={'class':'t-chart'})
tbody = tables.find('tbody')
table_rows = tbody.find_all('tr')

sample_dict = {}
sample_dict['date']=['1MO','2MO','6MO','1YR','2YR','3YR','5YR','7YR','10YR','20YR','30YR']
final_dict = {}

for tr in table_rows[1:] :
#     
    td_data = tr.find_all('td')
#     print(td_data)
    row = [i.text for i in td_data]
    interest_rate_list = row[1:]
#    print(interest_rate_list)
    sample_dict[row[0]]=interest_rate_list
   

print(sample_dict)
'''

# https://www.google.com/search?q=test&ie=&oe=

url='https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2018'
# url="file:///C:/Work/Projects/Python/eclipse-workspace/MATPLOT_LEARNING/Examples/basic_table.html"
# For https links you cannot use data
# values = {"data":"yieldYear","year":"2018"}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0'
headers = {'User-Agent': user_agent}
request = Request(url,headers=headers)
html = urlopen(request).read()
# print(str(html))


soup = bs.BeautifulSoup(html,'html5lib') 
table_data = soup.find_all('table', class_='t-chart')
print(table_data.contents[0])
# print(len(list(table_data)))


# print(soup.encode("utf-8"))







    


# table_tag = beautifulSoupObject.find_all(["h2","hr"])
# print(table_tag)

# for tag in beautifulSoupObject.find_all(True):
#     print(tag.name)
# for tag in beautifulSoupObject.find_all(re.compile("^h")):
#     print(tag.name)

    
# beautifulSoupObject.find_all()



# rowlist = re.findall(r'<tbody>(.*?)</tbody>', str(html))
# print(rowlist)


# try:
# 
#     user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     headers = {'User-Agent': user_agent}
#     request = Request(url, headers=headers)
#     htmlstring = urlopen(request).read()
#     print(htmlstring)
# 
# #     first_tr=re.findall('r<tbody>.*?</tbody>', str(htmlstring))
# #     print(first_tr)
# #     
# except Exception as e:
#     
#     print(str(e))    



#df = pd.DataFrame(sample_list)
#print(df.head())
