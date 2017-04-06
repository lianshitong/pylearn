#!/usr/bin/env python
#coding:utf-8
#笨方法学py(第四版)
#习题 15: 读取文件

#导入sys模块中的argv功能
from sys import argv

#定义argv传参名称,默认第一个变量是文件本身的文件名
script,filename = argv

#定义一个变量txt，使用open函数打开一个file
txt = open(filename)

#打印argv获取到的文件名
print  "here's your file %r:" %filename

#把open(filename)文件中的内容read出来，然后打印到屏幕上
print txt.read()

#再次输入一个文件名
print "Type the filename again:"

#获取需要打开的文件名
file_again = raw_input(">")

#open需要打开的文件并赋值给变量txt_again
txt_again = open(file_again)

#read文件的内容并让print打印到屏幕
print txt_again.read()