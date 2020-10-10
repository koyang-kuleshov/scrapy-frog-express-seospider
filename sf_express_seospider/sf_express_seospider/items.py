import scrapy
from scrapy.loader.processors import TakeFirst


class SeoItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    status_code = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    header_1 = scrapy.Field()
