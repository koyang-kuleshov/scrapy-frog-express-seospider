# import pudb; pudb.set_trace()
import re
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose


def get_nodes(value):
    if value['nodes'].find('https://') > -1:
        spam = value['nodes'].replace(f'https://{value["domain"]}', '')
        if not spam:
            return '/'
    else:
        spam = value['nodes'].replace(f'http://{value["domain"]}', '')
        if not spam:
            return '/'
    return [el for el in spam.split('/') if el]


class SfExpressSeospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TreeNodeItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    status_code = scrapy.Field(output_processor=TakeFirst())
    nodes = scrapy.Field(output_processor=MapCompose(get_nodes))
