import scrapy


class QuickSpider(scrapy.Spider):
    name = 'quick'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
