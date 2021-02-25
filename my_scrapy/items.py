# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    now_time = scrapy.Field()
    amount = scrapy.Field()
    price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    s_code = scrapy.Field()
