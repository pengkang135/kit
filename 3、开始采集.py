from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


"""
#方式一：单页面爬取。直接查找所有连接
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
"""

"""
#方式二：单页面爬取。所有链接但去掉不必要的链接
#规则：
#  1、它们都在 id 是 bodyContent 的 div 标签里
#  2、URL 链接不包含冒号
#  3、URL 链接都以 /wiki/ 开头
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
"""


"""
# 方式三：随机逐个爬页面
# 1、代码封装在函数getLinks内。2、主函数调用：随机调用，直到没有新链接为止。
# 该段代码不会自动停止!

import datetime
import random
random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                     href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    
"""


"""
# 方式四：爬整站。由于网站内页面存在重复调用，方式三可能调用到重复页面。这里做了两点改动：
# 1、去重 2、除调用内部链接也调用外部。
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
"""



# 方式五：爬整站。爬虫和数据收集（至少是数据打印）的组合：
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)

    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")