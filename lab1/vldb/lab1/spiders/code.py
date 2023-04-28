import scrapy
from lab1.items import Lab1Item

class CodeSpider(scrapy.Spider):
    name = "code"
    allowed_domains = ["vldb.org/pvldb/volumes/15"]
    start_urls = ["http://vldb.org/pvldb/volumes/15"]

    def parse(self, response):
        items = []
        print("正在解析网页")

        # print(len(response.xpath('//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/div[4]/div[@id]')))
        # print(response.xpath(''))
        for father in response.xpath('//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/div[4]/div[@id]'):
            # print("father info",father)
            for each in father.xpath('./div[5]/div'):
                item = Lab1Item()
                title = each.xpath('./div/h5/text()').extract()
                author = each.xpath('./div/p[last()]/text()').extract()
                # print("打印文章题目信息",title[0])
                # print("打印作者信息",author[0])
                item['title'] = title[0]
                item['author'] = author[0]
                items.append(item)
        return items
