from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from iosicongallery.items import IosicongalleryItem

class IosiconSpider(Spider):
    name = 'iosicon'
    allowed_domains = ['iosicongallery.com']
    start_urls = ['http://iosicongallery.com/']    

    def parse(self, response):
        crawledLinks = []
        for link in SgmlLinkExtractor(restrict_xpaths='//div[@class="wp-pagenavi"]').extract_links(response):
            if not link.url in crawledLinks:
                crawledLinks.append(link.url)
                yield Request(link.url, callback = self.parse)

        for link in SgmlLinkExtractor(restrict_xpaths='//ul[@class="list-icons"]').extract_links(response):
            if not link.url in crawledLinks:
                crawledLinks.append(link.url)
                yield Request(link.url, callback = self.parse_detail)
#        sel = Selector(response)
#        refer_websites = sel.xpath('//@href').extract()
#        for weburl in refer_websites:
#            if weburl == response.url:
#                continue
#            yield Request(weburl, callback = self.parse)
        #i = IosicongalleryItem()
        #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        #return i
        
    
    def parse_detail(self, response):
        print ('---------------%s') % response.url
        sel = Selector(response)
        i = IosicongalleryItem()
        i['image_urls'] = sel.xpath('//li[@class="icon-container-512"]/img/@src').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        return i