#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by fengyuwusong at 2018/1/19
import pymysql
import random

__author__ = 'fengyuwusong'


class sqlHelper(object):
    def __init__(self, host, user, password, database):
        # 打开数据库连接
        self.db = pymysql.connect(host, user, password, database, use_unicode=True, charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    # 析构函数关闭连接
    def __del__(self):
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()

    # 插入数据库
    def insert(self, ip, port, type, location, protocol, updateTime):
        sql = "insert into proxy values(null,'%s',%s,'%s','%s','%s','%s')" % (
            ip, port, type, location, protocol, updateTime)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            print(ip, "插入成功~")
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    # 随机获取一条
    def getByRandom(self):
        sql = "SELECT count(*) FROM proxy"
        # 执行SQL语句
        self.cursor.execute(sql)
        # 获取代理长度
        results = self.cursor.fetchall()
        length = results[0][0]
        # 在其中随机获取一个
        i = random.randint(1, length)
        sql = "select * from proxy where id=%s" % i
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results[0][5].lower() + "://" + results[0][1] + ":" + str(results[0][2])


if __name__ == '__main__':
    mysql = sqlHelper("localhost", "root", "admin", "proxy")
    server = mysql.getByRandom()
    print(server)
