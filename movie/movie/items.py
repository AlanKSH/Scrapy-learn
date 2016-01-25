# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = Field()
    movie_director = Field()
    movie_writer = Field()
    movie_roles = Field()
    movie_Language = Field()
    movie_long = Field()
    movie_description = Field()
