# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from DaZhong.items import ProxyItem
import re

class ProxySpider(CrawlSpider):
    name = 'ProxySpider'
    allowed_domains = ['www.youdaili.cn']
    #==================Customer Def==========================
    indexes    = [2,3,4,5]
    date_id    = 2059
    start_urls = []
    start_urls.append('http://www.youdaili.cn/Daili/guonei/%s.html' % date_id)
    for i in indexes:
        url = 'http://www.youdaili.cn/Daili/guonei/%s_%s.html' % (date_id, i)
        start_urls.append(url)
    #==================Customer Def==========================
        

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        addresses = hxs.select('//div[@class="cont_font"]/p/text()').extract()
        items = []
        for address in addresses:
            item = ProxyItem()
            str1 = address.split(':')
            if str1:
                ip = str1[0].strip('\r').strip('\n')
                item['address'] = ip
                address = str1[1]
                str2 = address.split('@')
                if str2:
                    port = str2[0]
                    item['port'] = port
                    address = str2[1]
                    str3 = address.split('#')
                    if str3:
                        protocol = str3[0]
                        item['protocol'] = protocol
                        address = str3[1]
                        str4 = address.split(' ')
                        if len(str4) == 1:
                            item['location'] = str4[0]
                        elif len(str4) == 2:
                            item['location'] = str4[0]
                            item['type'] = str4[1]
            items.append(item) 
        return items