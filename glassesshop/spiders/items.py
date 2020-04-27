# -*- coding: utf-8 -*-
import scrapy


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        
        for items in response.xpath("//div[@class='prlist row']"):

            container = items.xpath(".//div[@class='col-sm-6 col-md-4 m-p-product']").get()
            print(container)
