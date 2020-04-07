# -*- coding: utf-8 -*-
import scrapy
from ..items import BbcItem
from lxml import html
import requests

class BbcSpiderSpider(scrapy.Spider):
    name = 'bbc_spider'
  #  allowed_domains = ['bbc.com']
  #   start_urls = ['https://www.bbc.com/news/world-europe-52165522']
    start_urls = ['https://www.theguardian.com/world/2020/apr/05/french-police-terrorism-inquiry-two-killed-stabbing-romans-sur-isere']

    def parse(self, response):
        items = BbcItem()
        page = requests.get(
            'https://www.theguardian.com/world/2020/apr/05/french-police-terrorism-inquiry-two-killed-stabbing-romans-sur-isere')
        # page = requests.get('https://www.bbc.com/news/world-europe-52165522')
        tree = html.fromstring(page.content)

        article_text = response.css('p::text').extract()
        items['article_text'] = article_text

        article__publisher = tree.xpath('//meta[@property="article:publisher"]/@content')
        items['article__publisher'] = article__publisher

        article_url = tree.xpath('//meta[@property="og:url"]/@content')
        items['article_url'] = article_url

        article_headline = tree.xpath('//meta[@property="og:title"]/@content')
        items['article_headline'] = article_headline

        article_tag = tree.xpath('//meta[@property="article:tag"]/@content')
        items['article_tag'] = article_tag

        article__published_time = tree.xpath('//meta[@property="article:published_time"]/@content')
        items['article__published_time'] = article__published_time

        article_author = tree.xpath('//meta[@property="article:author"]/@content')
        items['article_author'] = article_author

        yield items
