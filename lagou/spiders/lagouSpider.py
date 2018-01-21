# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem


class LagouspiderSpider(scrapy.Spider):
    name = 'lagouSpider'
    allowed_domains = ['www.lagou.com']
    start_urls = []

    for i in range(1, 30):
        start_urls.append('https://www.lagou.com/zhaopin/Java/2/?filterOption=' + str(i))

    def parse(self, response):
        items = []
        datas = response.xpath("//ul[@class='item_con_list']/li")
        for data in datas:
            item = LagouItem()
            item['name'] = data.xpath(".//a[@class='position_link']/h3/text()").extract()[0]
            item['location'] = data.xpath(".//a[@class='position_link']/span/em/text()").extract()[0]
            item['day'] = data.xpath(".//span[@class='format-time']/text()").extract()[0]
            item['companyName'] = data.xpath(".//div[@class='company_name']/a/text()").extract()[0]
            item['companyType'] = data.xpath(".//div[@class='industry']/text()").extract()[0].strip()
            item['salary'] = data.xpath(".//div[@class='li_b_l']/span[@class='money']/text()").extract()[0]
            item['require'] = data.xpath(".//div[@class='p_bot']/div[@class='li_b_l']/text()").extract()[2].strip()
            item['tag'] = str(data.xpath(".//div[@class='list_item_bot']/div[@class='li_b_l']/span/text()").extract())
            item['keyWord'] = data.xpath(".//div[@class='list_item_bot']/div[@class='li_b_r']/text()").extract()[0]
            items.append(item)
        return items
