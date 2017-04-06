#-*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 函数
def  printPlistCode():
    #1.得到这个网页的 html 代码 #
    html = urllib2.urlopen("http://movie.douban.com/chart").read()

    #2.转换 一种格式，方便查找
    soup = BeautifulSoup(html)
    #3.  得到 找到的所有 包含 a 属性是class = nbg 的代码块,数组
    liResutl = soup.findAll('div')
    assert isinstance(liResutl, )
    print liResutl
#     #4.用于拼接每个字典的字符串
#     tmpDictM = ''
#
#     #5. 遍历这个代码块  数组
#     for li in liResutl:
#
#         #5.1 找到 img 标签的代码块 数组
#         imageEntityArray = li.findAll('img')
#
#         #5.2 得到每个image 标签
#         for image in imageEntityArray:
#             #5.3 得到src 这个属性的 value  后面也一样 类似 key value
#             link = image.get('src')
#             imageName = image.get('alt')
#             #拼接 由于 py中 {} 是一种数据处理格式，类似占位符
#             tmpDict = '''@{0}@\"name\" : @\"{1}\", @\"imageUrl\" : @\"{2}\"{3},'''
#
#             tmpDict =  tmpDict.format('{',imageName,link,'}')
#
#             tmpDictM = tmpDictM + tmpDict
#
#     #6.去掉最后一个 ,
#     tmpDictM = tmpDictM[0:len(tmpDictM) - 1].decode('utf8')
#
#     #7 拼接全部
#     restultStr = '@[{0}];'.format(tmpDictM)
#
#     print restultStr
#
#
# if __name__ == '__main__':
#     printPlistCode()