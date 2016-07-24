# -*- coding:utf-8 -*-

import os
from scrapy import log
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from DaZhong.items import ShopItem

class DirInitializeSpider(Spider):
    name = 'DirInitializeSpider'
    allowed_domains = ['www.dianping.com']
    
    def __init__(self, category=None, *args, **kwargs):
        super(DirInitializeSpider, self).__init__(*args, **kwargs)
        self.basepath = "DaZhongData/Shops/"
        self.allcitys = open('allcitylist','r')
        self.foreign = open('foreign','a')
        self.urlhead = 'http://www.dianping.com'
        #for test
        self.start_urls = ['http://www.dianping.com/aba']
        
    def start_requests(self):
        requests = []
        for line in self.allcitys.readlines():
            strlst = line.strip('\n').split('\t')
            if len(strlst) == 3:
                cityname = strlst[1]
                urlend = strlst[2]
                url = self.urlhead + urlend.encode('utf8')
                #url quchong is finished
                arequest = Request(url, meta={'city': cityname,'requesturl':url},callback=self.parse)
                requests.append(arequest)
        return requests
    
    def parse(self, response):
        log.msg('==========+++++YelboshMessage+++++==========正在处理城市'+response.meta['city']+'........==========+++++YelboshMessage+++++==========')
        #log.msg('==========+++++YelboshMessage+++++=========='+response.url+'==========+++++YelboshMessage+++++==========')
        cityname = response.meta['city']
        #cityname = '阿坝'
        #if 1 == 2:
        if response.meta['requesturl'] != response.url:
            #self.foreign.write(response.meta['city']+'\t'+response.url+'\n')
            pass
        else:
            hxs = HtmlXPathSelector(response)
            rootmenulst = hxs.select('//ul[@id="G_chan-panel"]/li')
            #直接根据html
            if rootmenulst:
                for rootli_node in rootmenulst:
                    #the big class's name
                    bigClassName = rootli_node.select('./a/span/text()').extract()
                    #self.foreign.write(bigClassName[0].encode("utf8")+'\n')
                    #to each big class there are a lot of small class to each city
                    childmenulst = rootli_node.select('./ul/li')
                    for childli_node in childmenulst:
                        #to create the accorded directory
                        smallClassName = childli_node.select('./a/text()').extract()
                        smallClassUrl = childli_node.select('./a/@href').extract()
                        #self.foreign.write('\t'+smallClassName[0].encode("utf8")+'\n')
                        #create the small class directory and file
                
                        #if small class dir exists
                        path1 = self.basepath + bigClassName[0].encode("utf8") + '/' + cityname
                        if os.path.exists(path1):#like './DaZhongData/Shops/美食/北京'
                            pass
                        else:
                            os.makedirs(path1)
                        #open the index file for each city of different small class , and write the index into it 
                        pathfile = path1 + '/index'
                        indexfile = open(pathfile,'a')
                        indexfile.write(smallClassName[0].encode("utf8") + '\t' + smallClassUrl[0].encode("utf8") + '\n')
                        #if small class index file exists
                        path2 = path1 + '/' + smallClassName[0].encode("utf8")
                        if os.path.exists(path2):#like './DaZhongData/Shops/美食/北京/北京菜'
                            pass
                        else:
                            os.makedirs(path2)
                        pass
                    pass
                pass
            else:#通过js脚本加载，用正则表达式进行匹配
                rootmenulst = hxs.select('//*[@id="leftCategory_ul"]/li/ul/li[2]/ul/li/ul/li')
                if rootmenulst:
                    self.foreign.write(response.meta['city']+'\t'+response.url+'\n')
                for rootli_node in rootmenulst:
                    #the big class's name
                    bigClassName = rootli_node.select('./a/text()').extract()
                    #self.foreign.write(bigClassName[0].encode("utf8")+'\n')
                    #to each big class there are a lot of small class to each city
                    childmenulst = rootli_node.select('./ul/li')
                    for childli_node in childmenulst:
                        #to create the accorded directory
                        smallClassName = childli_node.select('a/text()').extract()
                        smallClassUrl = childli_node.select('a/@href').extract()
                        #self.foreign.write('\t'+smallClassName[0].encode("utf8")+'\n')
                        #create the small class directory and file
                
                        #if small class dir exists
                        path1 = self.basepath + bigClassName[0].encode("utf8") + '/' + cityname
                        if os.path.exists(path1):#like './DaZhongData/Shops/美食/北京'
                            pass
                        else:
                            os.makedirs(path1)
                        #open the index file for each city of different small class , and write the index into it 
                        pathfile = path1 + '/index'
                        indexfile = open(pathfile,'a')
                        indexfile.write(smallClassName[0].encode("utf8") + '\t' + smallClassUrl[0].encode("utf8") + '\n')
                        #if small class index file exists
                        path2 = path1 + '/' + smallClassName[0].encode("utf8")
                        if os.path.exists(path2):#like './DaZhongData/Shops/美食/北京/北京菜'
                            pass
                        else:
                            os.makedirs(path2)
                        pass
                    pass
                pass
