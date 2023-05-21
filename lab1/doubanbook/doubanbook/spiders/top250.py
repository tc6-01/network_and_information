import requests
import scrapy
from doubanbook.items import DoubanbookItem
from lxml import etree
from time import sleep
class Top250Spider(scrapy.Spider):
    start_urls = []
    for x in range(50):
        # http://wjw.gz.gov.cn/ztzl/xxfyyqfk/yqtb/index_50.html
        if(x == 0):
            url = "http://wjw.gz.gov.cn/ztzl/xxfyyqfk/yqtb/index.html"
        else:
            url = 'http://wjw.gz.gov.cn/ztzl/xxfyyqfk/yqtb/index_' + str(x + 1) + '.html'
        start_urls.append(url)
    def parse(self, response):
        url_list  = []
        items = []
        print("正在解析网页")
        print("-------------------------")
        # 存入url列表
        for father in response.xpath("/html/body/div/div[3]/div[3]/div[2]/ul/li/div[@class='title']/a"):
            url = father.xpath("@href").extract()
            url_list.append(url)
            # print("Book title",bookTitle)
            # print("Book info",info[0])
        # print(len(items))
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36"
        }
        for url in url_list:
            rep = requests.get(url, headers=headers)
            item = DoubanbookItem()
            html = etree.HTML(rep.text)
            new = html.xpath("/html/body/div/div[3]/div[3]/div[2]/div[2]/p[1]")
            Date = html.xpath("/html/body/div/div[3]/div[3]/div[2]/div[1]/div[1]/span[1]/b")
            item['new'] = new
            item['date'] = Date[0]
        return items

