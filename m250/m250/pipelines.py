# -*- coding: utf-8 -*-

import json
import codecs
from os import path
from scrapy import signals


class M250Pipeline(object):
    def __init__(self):
        self.file = codecs.open('raw_data.txt', 'w', "utf-8")

    def process_item(self, item, spider):
        self.file.write(u'Top'+item['rank'][0]+'\n')
        self.file.write(u'《'+item['title'][0]+u'》'+'\n')
        self.file.write(u'链接:'+item['link'][0]+'\n')
        self.file.write(u'评分:'+item['rate'][0]+'\n')
        self.file.write(u'评语:'+item['quote'][0]+'\n'+'\n')
        return item
        file.close

