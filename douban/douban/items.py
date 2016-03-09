from scrapy import Field, Item


class DbprofileItem(Item):
    title = Field()
    intro = Field()
    location = Field()
    date = Field()
    bookdo = Field()
    bookwish = Field()
    bookcollect = Field()
    moviedo = Field()
    moviewish = Field()
    moviecollect =Field()
    musicdo = Field()
    musicwish = Field()
    musiccollect = Field()
    gamedo = Field()
    gamewish = Field()
    gamecollect = Field()
    review  = Field()