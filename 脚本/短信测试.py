#coding:utf-8

#云融正通短信平台测试


import urllib2
import urllib


body = []
for i in body:
    #print i
    url = 'http://101.201.238.246/MessageTransferWebAppJs/servlet/messageTransferServiceServletByXml?userName=usernamey&passWord=password&cmd=sendMessage&mobilePhone=15950032737&body='
    post_url = str(url + i)
    #print post_url

    # 提交，发送数据
    req = urllib2.urlopen(post_url)

