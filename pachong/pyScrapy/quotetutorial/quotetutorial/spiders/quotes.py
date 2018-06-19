# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.tosacrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print(response.text)
