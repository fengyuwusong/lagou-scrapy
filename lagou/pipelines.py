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
        # today = time.strftime("%Y%m%d", time.localtime())
        # fileName = today + ".txt"
        # with open(fileName, 'a', encoding='utf8') as fp:
        #     fp.write(item['name'] + '\t')
        #     fp.write(item['salary'] + '\t')
        #     fp.write(item['require'] + '\t')
        #     fp.write(item['tag'] + '\t')
        #     fp.write(item['companyName'] + '\t')
        #     fp.write(item['companyType'] + '\t')
        #     fp.write(item['location'] + '\t')
        #     fp.write(item['keyWord'] + '\t')
        #     fp.write(item['day'] + '\t')
        # fp.write("\n")
if __name__ == '__main__':
    sql = sqlHelper("localhost", "root", "admin", "lagou")
    item={'companyName': '分乐惠',
          'companyType': '移动互联网,数据服务 / 不需要融资',
          'day': '1天前发布',
          'keyWord': '“项目分成”',
          'location': '天津·王顶堤',
          'name': 'JAVA',
          'require': '经验3-5年 / 本科',
          'salary': '10K-20K',
          'tag': "['C#/.NET', 'Node.js']"}
    sql.insert(item['name'], item['salary'], item['require'], item['tag'], item['companyName'], item['companyType'],
               item['location'], item['keyWord'], item['day'])