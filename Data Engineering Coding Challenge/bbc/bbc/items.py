# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BbcItem(scrapy.Item):
    # define the fields for your item here like:
    article_text = scrapy.Field()
    article_author = scrapy.Field()
    article__publisher = scrapy.Field()
    article_headline = scrapy.Field()
    article_url = scrapy.Field()
    article_tag = scrapy.Field()
    article__published_time = scrapy.Field()

    pass
