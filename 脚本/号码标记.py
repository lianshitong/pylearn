#coding:utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup


url = 'https://www.so.com/s?q=051286865112'

# 提交，发送数据
req = urllib2.urlopen(url)


# 获取提交后返回的信息
content = BeautifulSoup(req)


a = content.prettify()
print a.find("span")

