#coding = utf-8
#第 0008 题：一个HTML文件，找出里面的正文。

#专门找了一个有中文的网址，尝试处理中文问题
import requests
from bs4 import BeautifulSoup

url = 'http://cn.python-requests.org/zh_CN/latest/'
html = requests.get(url)
# html的编码格式为'ISO-8859-1',通过html.encoding可以查看
# 有两种方式可以获取网页内容：
# 1.html.text,得到一个字符串str，内容为网页结构，但需要根据网页编码进行重新编码和解码才能显示中文
page = html.text.encode('ISO-8859-1').decode('utf-8')
# 2.html.content,得到的格式为bytes,直接解码
page = html.content.decode('utf-8')

#最后
soup = BeautifulSoup(page,'lxml')
print (soup.body.text)