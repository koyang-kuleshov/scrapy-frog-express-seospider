# import pudb; pudb.set_trace()
import scrapy
from scrapy.exceptions import NotSupported
from scrapy.loader import ItemLoader
from sf_express_seospider.items import TreeNodeItem

from common.images_format import IMAGES_FORMATS as IMAGES


class TreeScanerSpider(scrapy.Spider):
    name = 'tree_scaner'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def __init__(self, domain: str, *args, **kwargs):
        self.allowed_domains = [domain]
        self.start_urls = [f'https://{domain}']
        self.link_counter = 1
        super().__init__(*args, **kwargs)

    def parse(self, response):
        item = ItemLoader(TreeNodeItem(), response)
        item.add_value('url', response.url)
        item.add_value('nodes', {'domain': self.allowed_domains[0],
                                 'nodes': response.url}
                       )
        item.add_value('status_code', response.status)
        for url in response.xpath('//a/@href'):
            try:
                if url.get().split('.')[-1] not in IMAGES:
                    yield response.follow(url, callback=self.parse)
            except ValueError:
                pass

        yield item.load_item()
