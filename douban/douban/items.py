from scrapy import Field, Item


class DbprofileItem(Item):
    title = Field()
    intro = Field()
