from utils.argparser import read_params
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Settings

from sf_express_seospider import settings
from sf_express_seospider.spiders.quick import QuickSpider
from sf_express_seospider.spiders.tree_scaner import TreeScanerSpider

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    crawler_proc = CrawlerProcess(settings=crawler_settings)

    params = read_params()
    domain = params['domain']
    if not params['quick'] and not params['tree']:
        pass
    elif not params['quick'] and params['tree']:
        crawler_settings['CONCURRENT_REQUESTS'] = 32
        crawler_settings['DOWNLOAD_DELAY'] = 1
        crawler_settings['CONCURRENT_REQUESTS_PER_DOMAIN'] = 32
        crawler_settings['CONCURRENT_REQUESTS_PER_IP'] = 32
        crawler_proc.crawl(TreeScanerSpider, domain)
    else:
        crawler_settings['LOG_ENABLED'] = False
        crawler_settings['CONCURRENT_REQUESTS'] = 32
        crawler_settings['DOWNLOAD_DELAY'] = 0.1
        crawler_settings['CONCURRENT_REQUESTS_PER_DOMAIN'] = 32
        crawler_settings['CONCURRENT_REQUESTS_PER_IP'] = 32
        crawler_proc.crawl(QuickSpider, domain)

    crawler_proc.start()
