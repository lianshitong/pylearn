#!/usr/bin/env python
#coding:utf-8
#笨方法学py(第四版)
#习题 21 函数可以返回的东西

def add(a,b):
    print "adding %d + %d "%(a,b)
    return a + b

def subtract(a,b):
    print "subtracting %d - %d "%(a,b)
    return a - b

def multiply(a,b):
    print "multiplyting %d * %d "%(a,b)
    return a * b

def divide(a,b):
    print "dividing %d / %d "%(a,b)
    return a / b

print "let's do some marh with just functions!"
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print  "Age:%d,Height:%d,Weight%d,IQ:%d"%(age,height,weight,iq)


print "here is a puzzle."

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
print "that becomes:",