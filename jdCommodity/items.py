# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCommodityItem(scrapy.Item):
    image_urls = scrapy.Field()  # 指定文件下载的连接
    images = scrapy.Field()  # 文件下载完成后会往里面写相关的信息
    name = scrapy.Field()
