# -*- coding: utf-8 -*-
import json
import codecs
from os import path
from scrapy import signals

class DbprofilePipeline(object):
    def __init__(self):
        self.file = codecs.open('profile.txt','w',"utf-8")

    def process_item(self, item, spider):
        dict = {'book':u'书籍','movie':u'电影','music':u'音乐','game':u'游戏'}
        self.file.write(item['title'][0].strip()+'\n')
        self.file.write(u'居住于'+item['location'][0]+'\n')
        self.file.write(u'于'+item['date'][0].strip()+u'豆瓣'+'\n'+'\n')
        
        for x in ['book','movie','music','game']:
            self.file.write(dict[x]+u'：')
            for y in ['do','wish','collect']:
                if item[x+y]:
                    self.file.write(item[x+y][0]+u'，')
            self.file.write('\n')
        
        self.file.write('\n'+u'个人简介：'+'\n')
        for i in item['intro']:
            self.file.write(i+'\n')
        return item
        file.close
