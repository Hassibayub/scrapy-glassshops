# -*- coding: utf-8 -*-
import scrapy


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']


    # com = div[@class='col-sm-6 col-md-4 m-p-product']/div[@class="pimg default-image-front"]/a/img[@src]

    def parse(self, response):
      
        for items in response.xpath("//div[@class='col-sm-6 col-md-4 m-p-product']"):

            item_url = items.xpath(".//div[@class='pimg default-image-front']/a/@href").get()
            img_url = items.xpath(".//div[@class='pimg default-image-front']/a/img").get()
            item_name = items.xpath(".//div[@class='row']/p/a/text()").get()
            price = items.xpath(".//div[@class='row']/div/span/text()").get()


            yield {
                "item_url" : item_url,
                "img_url" : img_url,
                "item_name": item_name,
                "price": price
            } 
        
        next_page = response.xpath("(//li[@class='page-item'])[4]/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback= self.parse)
            
