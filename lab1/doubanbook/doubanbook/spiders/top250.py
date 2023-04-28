import scrapy
from doubanbook.items import DoubanbookItem

class Top250Spider(scrapy.Spider):
    name = "top250"
    allowed_domains = ["book.douban.com/top250"]
    start_urls = []
    for x in range(10):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)
    def parse(self, response):
        items = []
        print("正在解析网页")
        print("-------------------------")
        for father in response.xpath("//div[@class='article']/div[@class='indent']/table/tr/td[2]"):
            item = DoubanbookItem()
            score = father.xpath('./div[2]/span[2]/text()').extract()
            supply = father.xpath('./p[2]/span/text()').extract_first()
            info = father.xpath('./p[1]/text()').extract()
            bookTitle = father.xpath("./div[1]/a/text()").extract_first().strip()
            item['score'] = score[0]
            item['supply'] = supply
            item['bookTitle'] = bookTitle
            item['info'] = info[0]
            items.append(item)
            # print("Book title",bookTitle)
            # print("Book info",info[0])
        # print(len(items))
        return items

