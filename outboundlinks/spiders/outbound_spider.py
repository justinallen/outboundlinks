"""Spider to recursively crawl a website and extract outbound links."""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urlparse
from outboundlinks.items import OutboundlinksItem


class OutboundSpider(CrawlSpider):
    """
    Spider that crawls a website recursively and extracts outbound (external) links.
    
    Usage:
        scrapy crawl outbound -a start_url=https://example.com -o outbound_links.csv
    """
    name = 'outbound'
    
    def __init__(self, start_url=None, *args, **kwargs):
        """
        Initialize the spider with a start URL.
        
        Args:
            start_url: The URL to start crawling from
        """
        super(OutboundSpider, self).__init__(*args, **kwargs)
        
        if not start_url:
            raise ValueError("start_url argument is required. Usage: scrapy crawl outbound -a start_url=https://example.com")
        
        self.start_urls = [start_url]
        
        # Extract the domain from start_url to define allowed_domains
        parsed_url = urlparse(start_url)
        self.allowed_domains = [parsed_url.netloc]
        self.start_domain = parsed_url.netloc
        
        # Define rules for crawling
        # Follow all links within the same domain
        self.rules = (
            Rule(
                LinkExtractor(allow_domains=self.allowed_domains),
                callback='parse_page',
                follow=True
            ),
        )
        super(OutboundSpider, self)._compile_rules()
    
    def parse_page(self, response):
        """
        Parse a page and extract all outbound (external) links.
        
        Args:
            response: The response object from the crawled page
            
        Yields:
            OutboundlinksItem: Items containing outbound links and source pages
        """
        # Get the current page URL
        source_page = response.url
        
        # Extract all links from the page
        link_extractor = LinkExtractor()
        all_links = link_extractor.extract_links(response)
        
        # Filter for outbound links (links to different domains)
        for link in all_links:
            link_domain = urlparse(link.url).netloc
            
            # Check if the link is to a different domain (outbound)
            if link_domain and link_domain != self.start_domain:
                item = OutboundlinksItem()
                item['outbound_link'] = link.url
                item['source_page'] = source_page
                yield item
