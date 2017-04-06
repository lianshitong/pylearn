#!/usr/bin/env python
# coding:utf-8
# 笨方法学py(第四版)
# 习题 17: 更多文件操作

from sys import argv
# exists:检测文件是否存在,存在返回True,不存在返回False
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s " % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "the input file is %d bytes long" % len(indata)
print "Does the output file exist?%r" % exists(to_file)

print "ready,hit RETURN to continue,CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright,all done."

output.close()
input.close()
