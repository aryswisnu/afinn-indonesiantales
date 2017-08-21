from scrapy.item import Item, Field

class CeritaSampleItem(Item):
    link = Field()
    cerita = Field()
    judul = Field()