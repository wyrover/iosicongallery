#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
from scrapy.spider import Spider
from scrapy.utils.url import urljoin_rfc
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from iosicongallery.items import IosicongalleryItem
import urllib2
import urllib
import re
#import globalfunc

class IosIconSpider(Spider):
    name = "iosicongallery"
    allowed_domains = ["iosicongallery.com"]
    start_urls = ["http://iosicongallery.com/"]

    def parse (self, response):
        print response.url
        #		hxs = HtmlXPathSelector(response)
        #		refer_websites = hxs.select('//@href').extract()
        #
        #		if response.url.find("drivers") > 0:
        #			self.ParseDriverXML(response.url)
        #			return
        #
        #		for weburl in refer_websites:
        #			if weburl == response.url:
        #				continue
        #			utf8_url = weburl.encode('utf-8')
        #			#print weburl
        #			relink = re.compile("\/.*?cnbsd1\/product.*[^\?\&]",re.I)
        #			
        #			if relink.match(weburl):
        #				if not utf8_url.startswith('http://'):
        #					weburl = 'http://'+self.gethostname(response.url)+'/'+weburl
        #				
        #				weburl = re.sub(r'/\.\./\.\./',r'/',weburl)
        #				weburl = re.sub(r'/\.\./',r'/',weburl)
        #				self.saveFile(weburl)
        #				yield Request(weburl, callback=self.parse)

#        def gethostname (self, res_url):
#            proto, rest = urllib.splittype(res_url)
#            host, rest = urllib.splithost(rest)
#            return host
#
#        def saveFile (self, url):
#            self.f_write.write(url)
#            self.f_write.write('\n')
#
#        def ParseDriverXML (self, url):
#            pos = url.rfind("/")
#            filename = url[0:pos]
#            pos1 = filename.rfind("/")
#            filename = filename[pos1 + 1:pos]
#            driver_url = "http://www.dell.com/support/home/cn/zh/cnbsd1/product-support/product/"+filename + "/drivers"
#            print driver_url
#            htmlpage = globalfunc.OpenUrl(driver_url)
#            reLink = re.compile (r"type=\"hidden\"\s(.*)driversdata", re.I)
#            matchList = reLink.findall(htmlpage)
#
#            if matchList:
#                filepath = "data\\dell\\"+filename
#                globalfunc.SaveDriverInfo (filepath, driver_url, matchList[0])

#        def __init__ (self):
#            self.f_write = open ('visitedsites', 'w')
#
#        def __del__ (self):
#            self.f_write.close()
