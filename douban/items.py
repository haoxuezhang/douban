# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    score = scrapy.Field()
    movie_id = scrapy.Field()
    category=scrapy.Field()
    director = scrapy.Field()
    scriptwriter = scrapy.Field()
    movie_category = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    byname = scrapy.Field()
    
