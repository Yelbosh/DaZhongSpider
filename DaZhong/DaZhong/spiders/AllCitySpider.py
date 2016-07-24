# -*- coding:utf-8 -*-

import json
from scrapy import log
from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from DaZhong.items import CityItem

class AllCitySpider(CrawlSpider):
    name = 'AllCitySpider'
    allowed_domains = ['dianping.com']
    start_urls = ['http://dianping.com/citylist']
    
    rules = (  
        Rule(SgmlLinkExtractor(allow=(r'http://www.dianping.com/citylist')), callback="parse_item"),  
    )      
    
    #process the normal item elements
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//ul[@id="divPY"]/li')
        
        index = 1
        for link in links:
            linksPY = link.select('div/a')
            for linkPY in linksPY:
                item = CityItem()
                item['id'] = index
                item['name'] = linkPY.select('.//text()').extract()
                item['url'] = linkPY.select('@href').extract()
                if item['name']:
                    index = index + 1
                yield item
            #construct the AJAX source URL
            linkAJAX =  link.select('strong/text()').extract()#must not add the '/'
            try:
                urlAJAX = 'http://www.dianping.com/ajax/json/index/citylist/getCitylist?do=getByPY&firstPY=' + linkAJAX[0]
                request =  Request(urlAJAX, callback=self.parse_ajax)  
                yield request 
            except Exception , e:
                log.msg('==========+++++YelboshException+++++=========='+str(e)+'==========+++++YelboshException+++++==========')
        pass
    
    #process the ajax item elements
    def parse_ajax(self, response):
        AjaxObject = json.loads(response.body)
        jsonhtml = AjaxObject['msg']['html']
        sel = Selector(text=jsonhtml, type="html")
        links = sel.select('//a')
        for link in links:
            item = CityItem()
            item['id'] = 0
            item['name'] = link.select('text()').extract()
            item['url'] = link.select('@href').extract()
            yield item
        pass
