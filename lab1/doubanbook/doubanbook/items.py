# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#     书籍标题、主要信息、评分、总结等信
# 息（注意需要爬取250本书籍）
    # 新增病例 
    new = scrapy.Field()
    date = scrapy.Field()
