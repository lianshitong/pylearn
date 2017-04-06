#!/usr/bin/env python
#coding:utf-8

import os
import sys
import MySQLdb
from prettytable import PrettyTable
db_hostip = '127.0.0.1'
db_username = 'root'
db_passwd = '123456'
db_name = 'mysql'
try:
	acc = raw_input('Please input accname:').strip()
	conn=MySQLdb.connect(db_hostip,db_username,db_passwd,db_name,port=3306)
	cur=conn.cursor()
	cur.execute("select host,user,password from user where user='%s'" %acc)
	jilu = cur.fetchone()
