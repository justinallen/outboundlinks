# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OutboundlinksItem(scrapy.Item):
    """Item for storing outbound links and their source pages."""
    outbound_link = scrapy.Field()
    source_page = scrapy.Field()
