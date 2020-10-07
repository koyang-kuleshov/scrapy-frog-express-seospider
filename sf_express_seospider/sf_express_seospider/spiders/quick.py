from scrapy.spiders import SitemapSpider


class QuickSpider(SitemapSpider):
    name = 'quick'
    sitemap_urls = []

    def __init__(self, domain: str, *args, **kwargs):
        self.allowed_domains = [domain]
        self.sitemap_urls = [f'https://{domain}/sitemap.xml']
        self.link_counter = 1
        super().__init__(*args, **kwargs)

    def parse(self, response):
        print(f'{self.link_counter} : {response.url}')
        self.link_counter += 1
