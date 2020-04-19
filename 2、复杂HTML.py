from urllib.request import urlopen
from bs4 import BeautifulSoup

print("\n【标签：】")
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

# nameList = bsObj.findAll("span", {"class":"green"})
nameList = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
for name in nameList:
    print(name.get_text())


print("\n【导航树：】")
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

"""
# 子标签
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)
    
"""
"""
# 后代标签
for descendant in bsObj.find("table", {"id": "giftList"}).descendants:
    print(descendant)
"""

"""
# 兄弟标签
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    
"""

# 父标签
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
                       }).parent.previous_sibling.get_text())


import re
print("\n【正则表达式：】")
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])


print("\n【获取属性：】")
images = bsObj.findAll("img")
for image in images:
    print(image.attrs["src"])


print("\n【使用lambda：】")
mytags = bsObj.find(lambda tag: len(tag.attrs) == 2)
print(mytags)
