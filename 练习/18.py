#!/usr/bin/env python
#coding:utf-8
#笨方法学py(第四版)
#习题 18: 命名、变量、代码、函数


#def定义函数的关键字
def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r,arg2:%r" %(arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r" %(arg1,arg2)


def print_one(arg1):
    print "arg1:%r"%arg1

def print_none():
    print "i got nothin'."
print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first")
print_none()