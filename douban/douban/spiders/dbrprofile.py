import scrapy
from douban.items import DbprofileItem
import time
from scrapy.http.request import Request  

class DbprofileSpider(scrapy.spiders.Spider):
    name = "dbprofile"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/people/48335885/",
    ]

    def start_requests(self):  
        for url in self.start_urls:          
            yield Request(url, cookies={'_pk_id.100001.3ac3':'4ff929e3b35ff736.1452662726.3.1452746854.1452667708.', 
                                        '__utmb':'81379588.1.10.1452746854'})  

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        for sel in response.xpath('//html'):
            item = DbprofileItem()
            item['title'] = sel.xpath('//head/title/text()').extract()
            item['intro'] = sel.xpath('//*[@id="intro_display"]/text()').extract()
            yield item
            time.sleep(2)
