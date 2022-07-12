import scrapy


class DrugSpider(scrapy.Spider):
    name = 'drug'
    allowed_domains = ['mosbatesabz.com']
    start_urls = ['http://mosbatesabz.com/']

    def parse(self, response):
        pass
