import scrapy
from douban.items import DbprofileItem
import time
from scrapy.http.request import Request  

class DbprofileSpider(scrapy.spiders.Spider):
    name = "dbprofile"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/people/3028932/",
    ]

    #def start_requests(self):  
    #    for url in self.start_urls:          
    #        yield Request(url, cookies={''})  

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        for sel in response.xpath('//html'):
            item = DbprofileItem()
            item['title'] = sel.xpath('//head/title/text()').extract()
            item['intro'] = sel.xpath('//*[@id="intro_display"]/text()').extract()
            item['location'] = sel.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a/text()').extract()
            item['date'] = sel.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/div/text()[2]').extract()
            item['bookdo'] = sel.xpath('.//*[@id="book"]/h2/span/a[1]/text()').extract()
            item['bookwish'] = sel.xpath('.//*[@id="book"]/h2/span/a[2]/text()').extract()
            item['bookcollect'] = sel.xpath('.//*[@id="book"]/h2/span/a[3]/text()').extract()
            item['moviedo'] = sel.xpath('.//*[@id="movie"]/h2/span/a[1]/text()').extract()
            item['moviewish'] = sel.xpath('.//*[@id="movie"]/h2/span/a[2]/text()').extract()
            item['moviecollect'] = sel.xpath('.//*[@id="movie"]/h2/span/a[3]/text()').extract()
            item['musicdo'] = sel.xpath('.//*[@id="music"]/h2/span/a[1]/text()').extract()
            item['musicwish'] = sel.xpath('.//*[@id="music"]/h2/span/a[2]/text()').extract()
            item['musiccollect'] = sel.xpath('.//*[@id="music"]/h2/span/a[3]/text()').extract()
            item['gamedo'] = sel.xpath('.//*[@id="game"]/h2/span/a[1]/text()').extract()
            item['gamewish'] = sel.xpath('.//*[@id="game"]/h2/span/a[2]/text()').extract()
            item['gamecollect'] = sel.xpath('.//*[@id="game"]/h2/span/a[3]/text()').extract()
            item['review'] = sel.xpath('.//*[@id="review"]/h2/span/a/text()').extract()    
            yield item
            time.sleep(2)
