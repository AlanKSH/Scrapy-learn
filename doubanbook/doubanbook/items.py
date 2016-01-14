from scrapy import Field, Item


class DbbookItem(Item):
    title = Field()
    intro = Field()
