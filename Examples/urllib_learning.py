from urllib.request import Request, urlopen
import urllib.parse

# https://www.google.com/search?q=test&ie=&oe=

url='https://pythonprogramming.net/search'
values = {'q':'basic'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

# urlReq = urllib.request.Request(url,data)
# urlRes = urllib.request.urlopen(url)
# 
# print(urlRes.read())    

try:

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    request = Request(url,data, headers=headers)
    html = urlopen(request).read()
    print(html)

except Exception as e:
    
    print(str(e))    
    



