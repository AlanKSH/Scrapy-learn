#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from movie.items import MovieItem
import re 

class DoubanSpider(scrapy.Spider):
    name = "dbmovie"
    allowed_domains = ["movie.douban.com"]
    start_urls = []

    def start_requests(self):
        file_object = open('movie_name.txt','r')

        try:
            url_head = "http://movie.douban.com/subject_search?search_text="
            for line in file_object:
                self.start_urls.append(url_head + line)

            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        hxs = Selector(response)
        movie_link = hxs.xpath('//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[1]/a/@href').extract()

        if movie_link:
            yield Request(movie_link[0],callback=self.parse_item)

    def parse_item(self, response):
        hxs = Selector(response)
        movie_name = hxs.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        movie_director = hxs.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        movie_writer = hxs.xpath('/html/body/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]/span[2]/a[1]/text()').extract()
        movie_description = hxs.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()

        movie_roles_paths = hxs.xpath('//*[@id="info"]/span[3]/span[2]')
        movie_roles = []
        for movie_roles_path in movie_roles_paths:
            movie_roles = movie_roles_path.xpath('.//*[@rel="v:starring"]/text()').extract()

        item = MovieItem()
        item['movie_name'] = ''.join(movie_name).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') 
        item['movie_director'] = movie_director[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_director) > 0 else ''
        item['movie_description'] = movie_description[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_description) > 0 else ''
        item['movie_writer'] = ';'.join(movie_writer).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        item['movie_roles'] = ';'.join(movie_roles).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
        yield item