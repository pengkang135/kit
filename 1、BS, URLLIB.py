# BS4
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print("\n【Beautiful Soup:】")
print(bsObj.head)


# request
print("\n【request.urlopen:】")
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

# error
print("\n【urllib.error：】")
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)   # 异常2：500服务器不存在
    except HTTPError as e:    # 异常1：404网页不存在
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:   # 异常3：标签不存在
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)