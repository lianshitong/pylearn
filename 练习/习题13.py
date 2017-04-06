#!/usr/bin/env python
#coding:utf-8
#笨方法学py(第四版)
#习题 13: 参数、解包、变量
#运行此脚本的时候需要带上三个参数

#导入sys模块中的argv功能
from sys import argv

#定义参数变量
#argv 是所谓的“参数变量(argument variable)”
script,first,second,third = argv

#打印
print "The script is called:",script
print "Your first variable is:",first
print  "Your second variable is:",second
print  "Your third variable is:",third