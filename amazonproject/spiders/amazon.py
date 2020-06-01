# -*- coding: utf-8 -*-
import scrapy
# Now this code is the final code of the lecture
# In the lecture, as you see we are not getting results
# Based on your location you might actually get some good results here
# The problem is again the 'USER_AGENT'
# Now is the time we have a small discussion that will just follow from here...


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def start_requests(self):
        url = 'https://www.amazon.com/Unlocked-Cell-Phones-Android/s?rh=n%3A2407749011%2Cp_n_feature_twenty_browse-bin%3A17881876011'
        yield scrapy.Request(url)

    def parse(self, response):
        yield {'response': response.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()}
