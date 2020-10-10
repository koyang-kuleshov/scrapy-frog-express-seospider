import scrapy
from scrapy.loader import ItemLoader
from sf_express_seospider.items import SeoItem

from common.images_format import IMAGES_FORMATS as IMAGES


class SeoSpider(scrapy.Spider):
    name = 'tree_scaner'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def __init__(self, domain: str, *args, **kwargs):
        self.allowed_domains = [domain]
        self.start_urls = [f'https://{domain}']
        super().__init__(*args, **kwargs)

    def parse(self, response):
        item = ItemLoader(SeoItem(), response)
        item.add_value('url', response.url)
        item.add_value('status_code', response.status)
        item.add_value('title', response.xpath('//head/title/text()').extract())
        item.add_value('description',
                       response.xpath('//meta[@name="description"]/@content')
                       .extract())
        item.add_value('header_1', response.xpath('//h1/text()').extract())
        for url in response.xpath('//a/@href'):
            try:
                if url.get().split('.')[-1] not in IMAGES:
                    yield response.follow(url, callback=self.parse)
            except ValueError:
                pass

        yield item.load_item()
