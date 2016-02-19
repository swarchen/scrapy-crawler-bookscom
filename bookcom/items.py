# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookcomItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    publisher = scrapy.Field()
    pages = scrapy.Field()
    imgUrl = scrapy.Field()
    pass
