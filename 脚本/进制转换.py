#!/usr/bin/env python
#coding:utf-8

#二进制转换十进制
b = raw_input("please enter a binary number:")
d = 0
for i in range(0,len(b)):
    d = d + int(b[i] * (2 ** (len(b))-i-1))
    print d
