#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from movie.items import MovieItem
import re 

class DoubanSpider(BaseSpider):
