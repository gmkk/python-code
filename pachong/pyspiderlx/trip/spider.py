#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-06-15 11:49:17
# Project: TripAdvisor

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {
    }

    client = pymongo.MongoClient('localhost')
    db = client['trip']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.tripadvisor.cn/Attractions-g186338-Activities-c47-t163-London_England.html',
                   callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc(
                '#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)

        next = response.doc('#FILTERED_LIST > div.al_border.deckTools.btm > div > div > a').attr.href
        self.crawl(next, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        name = response.doc('.heading_title').text()
        rating = response.doc('.more > span').text()
        address = response.doc('.location > .address').text()
        phone = response.doc('.phone > div').text()
        duration = response.doc('.hours > .duration').text()

        return {
            "url": url,
            "name": name,
            "rating": rating,
            "address": address,
            "phone": phone,
            "duration": duration
        }

    def on_result(self, result):
        if result:
            self.save_to_mongo(result)

    def save_to_mongo(self, result):
        if self.db['London'].insert(result):
            print('插入MongoDB成功', result)
