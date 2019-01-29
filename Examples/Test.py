import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import sys

def run():
    r = requests.get('https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx/?data=yieldYear&year=2018')
    soup = BeautifulSoup(r.content,'html5lib')
    #
    tbl = soup.find_all('table')[1]
#     print(tbl)
    df = pd.read_html(str(tbl))
    print(df)
    #
#     df.columns = df.loc[0]
#     print(df.loc[0])
    #
#     cities = df['City'].tolist()
#     print(cities)

if __name__ == "__main__":
    run()