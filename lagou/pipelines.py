# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import pymysql


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
    def insert(self, name, salary, require, tag, companyName, companyType, location, keyWord, day):
        sql = "insert into lagou values(null,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
            name, salary, require, tag, companyName, companyType, location, keyWord, day)
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()


class LagouPipeline(object):
    def process_item(self, item, spider):
        sql = sqlHelper("localhost", "root", "admin", "lagou")
        sql.insert(item['name'], item['salary'], item['require'], item['tag'], item['companyName'], item['companyType'],
                   item['location'], item['keyWord'], item['day'])
        return item