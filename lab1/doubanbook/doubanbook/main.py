from scrapy import cmdline
cmdline.execute("scrapy crawl top250 -o doubanBookTop250.csv".split())