# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rating=scrapy.Field()
    age=scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    trip=scrapy.Field()
    departure_point=scrapy.Field()
    fare=scrapy.Field()
    availablity=scrapy.Field()
    image=scrapy.Field()
    
    
    