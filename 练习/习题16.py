#!/usr/bin/env python
#coding:utf-8

from sys import argv

script,filename = argv

print "we're going to erase %r." %filename
print "if you don't want that,hit CTRL-C(^C)"
print "if you do wang that,hit RETURN."

raw_input("?")

print "Opening the file....."
#打开文件,w是写入
target = open(filename,'w')

print "Truncating the file.Goodbye!"
#?
target.truncate()

print "Now i'm going to ask you for there lines."

#从用户端接收输入的内容
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "i'm going to write these to the file."

#把从用户端接收到的内容写入到对应的行中
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "And finally,we close it."
#写入完毕后,close文件
target.close()
