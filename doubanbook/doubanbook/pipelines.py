import json
import codecs
from os import path
from scrapy import signals

class DbbookPipeline(object):
    def __init__(self):
        self.file = codecs.open('raw_data.txt', 'w', "utf-8")

    def process_item(self, item, spider):
        self.file.write(item['title'][0]+'\n')
        for i in item['intro']:
            self.file.write(i+'\n')
        return item
        file.close
