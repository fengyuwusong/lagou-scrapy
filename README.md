# 使用说明
### 详细介绍请看博客：[风雨雾凇](http://blog.csdn.net/qq_33850908/article/details/79120203 "optional title")
- 环境准备：
1. python3.6
2. scrapy1.5
3. numpy
4. PIL
5. wordcloud
6. pymysql
7. jieba
具体安装教程请百度。
## 将unit目录放入你的python安装目录下的lib下。里面放着的是项目需要用到的header字典。
## 抓取数据
- 使用git下载完整项目后，打开**/lagou/lagou/pipelines.py**文件。修改第26、41行：
（建议数据库名为lagou，表名为lagou）
```python
      修改表名lagou
26    sql = "insert into lagou values(null,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
      #修改成你的数据库host和用户密码、数据库名
41    sql = sqlHelper("localhost", "root", "admin", "lagou")
```


- 在该项目文件目录下打开命令行，输入：
```
scrapy crawl lagouSpider
```

- 等待**5分钟**左右即可爬取完成并存入数据库中。
查看数据库：
![爬取结果](http://www.fengyuwusong.cn/img/git.jpg)

- 如果想抓取其他职业数据，将**/lagou/lagou/spiders/lagouSpider.py**第12行url改成对应职位：
```python
       #30改成对应总页数
11     for i in range(1, 30):
       #java
12     start_urls.append('https://www.lagou.com/zhaopin/Java/2/?filterOption=' + str(i))
       #python
12     start_urls.append('https://www.lagou.com/zhaopin/Python/2/?filterOption=' + str(i))
```
## 制作词云
- 打开**/chiyun/demo.py**,同样修改51行 的数据库相关代码后，运行，稍等片刻则可以出现结果。

![词云结果](http://img.blog.csdn.net/20180121140723028?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzM4NTA5MDg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- 制作其他关键词词云请修改**/chiyun/demo.py**,55行：
```python
54    for data in datas:
          # 2对应拉钩网每个职位的工资范围 （可以通过修改代码计算出平均范围）
          # 3对应拉钩网每个职位的最低要求
          # 4对应拉钩网每个职位的关键要求tag
          # 6对应拉钩网每个招聘公司类型
          # 8对应拉钩网招聘公司的关键词
55        text += data[4]
```
- 例如修改为8：得到结果图：
![词云结果](http://img.blog.csdn.net/20180121140733418?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzM4NTA5MDg=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

- 如果不喜欢这张图片或字体可以更换。将你想要生成的图片和字体放进该文件夹，修改/lagou/lagou/spiders/lagouSpider.py 第58、59行。
```python
      #更改为你放进去的字体和背景图名称
58    font = path.join(path.dirname(__file__), "xingshu.ttf")
59    background = np.array(Image.open(path.join(d, "demo.webp")))
```

