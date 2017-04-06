#!/usr/bin/env python
#coding:utf-8
#笨方法学py(第四版)
#习题 13: 提示和传递

from sys import argv

script,user_name = argv
#定义一个变量，把提示符设置成'>'
prompt = '>'


print "Hi %s,I'm the %s script."%(user_name,script)
print  "I'd like to ask you a faw questions."
print  "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "where do you live %s?"%user_name
#raw_input的提示符变成'>'
lives = raw_input(prompt)

print "whar kind of computer do you have?"
computer = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' %(likes, lives, computer)