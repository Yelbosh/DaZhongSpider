# -*- coding:utf-8 -*-

from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from DaZhong.items import CityItem

class CitySpider(Spider):
    name = 'CitySpider'
    allowed_domains = ['t.dianping.com']
    start_urls = ['http://t.dianping.com/citylist']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//div[@class="cityes-list"]/ul/li/div[@class="cityes"]/ul/li')
        
        index = 1
        for link in links:
            item = CityItem()
            item['id'] = index
            item['name'] = link.select('a/text()').extract()
            item['url'] = link.select('a/@href').extract()
            if item['name']:
                index = index + 1
            yield item
        pass
