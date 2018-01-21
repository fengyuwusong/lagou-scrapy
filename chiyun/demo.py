#!/usr/bin/env python

from os import path
import matplotlib.pyplot as plt
import pymysql
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import jieba


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

    # 随机获取一条
    def getAll(self):
        sql = "SELECT * FROM lagou"
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")


if __name__ == '__main__':
    sql = sqlHelper("localhost", "root", "admin", "lagou")
    datas = sql.getAll()
    print('开始加载文本')
    text = ''
    for data in datas:
        # 2对应拉钩网每个职位的工资范围 （可以通过修改代码计算出平均范围）
        # 3对应拉钩网每个职位的最低要求
        # 4对应拉钩网每个职位的关键要求tag
        # 6对应拉钩网每个招聘公司类型
        # 8对应拉钩网招聘公司的关键词
        text += data[4]
    text = text.replace("'", "")
    text = " ".join(jieba.cut(text))
    d = path.dirname(__file__)
    font = path.join(path.dirname(__file__), "xingshu.ttf")
    background = np.array(Image.open(path.join(d, "demo.webp")))
    print('加载图片成功！')
    wordcloud = WordCloud(background_color="white", max_words=200, font_path=font, width=300, height=150,
                          mask=background, max_font_size=500,
                          margin=2).generate(text)
    image_colors = ImageColorGenerator(background)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(background, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('生成词云成功!')
