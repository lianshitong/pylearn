#!/usr/bin/env python
# coding:utf-8

import MySQLdb
import time

#数据库信息
db_hostip = '127.0.0.1'
db_username = 'root'
db_passwd = '123456'
db_name = 'pydev'

# 打开数据库连接
db = MySQLdb.connect(db_hostip, db_username, db_passwd, db_name)

print "=======请输入您要处理日期======="
year = str(raw_input("年:"))
month = str(raw_input("月:"))
# day = str(raw_input("日:"))


# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = "SELECT count(*) FROM qz_log_telcenter WHERE time_add < '%s-%s-1 00:00:00'" % (year, month)
# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

# 提交，不然无法保存新建或者修改的数据
db.commit()


print "查询到:%s年%s月1日前一共有%s条数据." %(year,month,data)

choice = int(raw_input("是否执行删除动作?"))
# # print choice


if choice == 1:
    # print "成功删除"
    for i in range(1,32):
        sql = "DELETE FROM qz_log_telcenter WHERE time_add < '%s-%s-%s 00:00:00'" % (year, month,i)
        # 打开数据库连接
        db = MySQLdb.connect(db_hostip, db_username, db_passwd, db_name)

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 删除语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        print sql
        time.sleep(2)

else:
    print "退出脚本"

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 关闭数据库连接
db.close()
