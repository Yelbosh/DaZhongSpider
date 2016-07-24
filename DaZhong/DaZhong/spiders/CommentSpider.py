#-*- coding: UTF-8 -*-

import os
from scrapy import log
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from DaZhong.items import CommentItem
from scrapy.exceptions import DropItem


class CommentSpider(Spider):
    name = 'CommentSpider'
    
    def __init__(self, category=None, *args, **kwargs):
        super(CommentSpider, self).__init__(*args, **kwargs)
        self.basepath = "DaZhongData/Shops/"
        self.workpart = ['美食']
        self.urlhead = 'http://www.dianping.com/shop/'
        pass
        
    def init_Item(self,item):
        item['path'] = ''
        item['username'] = ''
        item['rankrst'] = ''
        item['usercontrib'] = ''
        item['average'] = ''
        item['rst1'] = ''
        item['rst2'] = ''
        item['rst3'] = ''
        item['content'] = ''
        item['recPro'] = []
        item['tags'] = []
        item['favorate_Pro'] = []
        item['specials'] = []
        item['car_stop'] = []
        item['atmosphere'] = []
        item['time'] = ''
        item['zan_count'] = ''
        item['reply_count'] = ''
        pass
    
    def lsttostr(self,lst):
        if lst:
            result = ''
            for item in lst:
                result += item.encode("utf8")
                return result
        else:
            return ''
        
    def start_requests(self):
        requests = []
        path0 = './DaZhongData/Shops'
        #construct the requests by the structure of the files
        for bigclass in self.workpart:
            #get the citydirs of this bigclass
            path1 = path0 + '/' + bigclass
            citydirs = os.listdir(path1)
            for city in citydirs:
                #get the index file and yield the requests according to it
                path2 = path1 + '/' + city
                smallclasses = os.listdir(path2)
                for smallclass in smallclasses:
                    path3 = path2 + '/' + smallclass
                    if os.path.isdir(path3):
                        items = os.listdir(path3)
                        for item in items:
                            path4 = path3 + '/' + item
                            if os.path.isdir(path4):
                                path5_1 = path4 + '/' + 'DefaultComments'
                                url_1 = self.urlhead + item + '/' + 'review_all'
                                path5_2 = path4 + '/' + 'TuanComments'
                                url_2 = self.urlhead + item + '/' + 'review_tuangou'
                                path5_3 = path4 + '/' + 'ShortComments'
                                url_3 = self.urlhead + item + '/' + 'review_short'
                                arequest1 = Request(url_1,meta={'path':path5_1,'type':'default'},callback=self.parse_pagelinks)
                                arequest2 = Request(url_2,meta={'path':path5_2,'type':'tuan'},callback=self.parse_pagelinks)
                                arequest3 = Request(url_3,meta={'path':path5_3,'type':'short'},callback=self.parse_pagelinks)
                                requests.append(arequest1)
                                requests.append(arequest2)
                                requests.append(arequest3)
        return requests
##        requests = []
##        url = 'http://www.dianping.com/shop/8988542/review_all'
##        url2 = 'http://www.dianping.com/shop/8988542/review_tuangou'
##        url3 = 'http://www.dianping.com/shop/8988542/review_short'
##        arequest = Request(url,meta={'path':'8988542/DefaultComments/','type':'default'},callback=self.parse_pagelinks)
##        arequest2 = Request(url2,meta={'path':'8988542/TuanComments/','type':'tuan'},callback=self.parse_pagelinks)
##        arequest3 = Request(url3,meta={'path':'8988542/ShortComments/','type':'short'},callback=self.parse_pagelinks)
##        #arequest = Request(url,meta={'path':'8988542/DefaultComments'},callback=self.parse_items)
##        requests.append(arequest)
##        requests.append(arequest2)
##        requests.append(arequest3)
##        return requests
        
    def parse_pagelinks(self,response):
        #log.msg('==========+++++YelboshMessage+++++========Processing  '+response.meta['path']+'........==========+++++YelboshMessage+++++==========')
        hxs = HtmlXPathSelector(response)
        baseurl = response.url
        pagermax = hxs.select('//div[@class="Pages"]/a[last()-1]/text()').extract()
        if pagermax:
            max = (int)(pagermax[0])
        else:
            max = 1
        pageindex = 1
        while pageindex < max+1:
            try:
                realurl = baseurl + '?pageno=' + str(pageindex)
                #request = Request(realurl,meta=response.meta,callback=self.parse_test)
                request = Request(realurl,meta=response.meta,callback=self.parse_items)
                yield request
                pageindex = pageindex + 1
            except Exception , e:
                self.track.write(request.url+'\n')
                raise DropItem(str(e))
        pass
        
    def parse_items(self, response):
        #the selector
        hxs = HtmlXPathSelector(response)
        
        if response.meta['type'] is not 'short':
            commentnodes = hxs.select('//div[@class="comment-list"]/ul/li')
            for commentnode in commentnodes:
                #initialize the item
                item = CommentItem()
                self.init_Item(item)
                item['path'] = response.meta['path']
                item['type'] = response.meta['type']
                item['username'] = self.lsttostr(commentnode.select('div[@class="pic"]/p[@class="name"]/a/text()').extract())
                item['usercontrib'] = self.lsttostr(commentnode.select('div[@class="pic"]/p[@class="contribution"]/span/@title').extract())
                basicinfos = commentnode.select('div[@class="content"]/div[@class="user-info"]/span')
                if len(basicinfos) == 2:
                    item['rankrst'] = self.lsttostr(basicinfos[0].select('@class').extract())[-2:]
                    item['average'] = self.lsttostr(basicinfos[1].select('text()').extract())
                rsttexts = commentnode.select('div[@class="content"]/div[@class="user-info"]/div[@class="comment-rst"]/span[@class="rst"]/em[@class="col-exp"]/text()').extract()
                #assign the rankgrade of the item
                if len(rsttexts) > 0:
                    item['rst1'] = rsttexts[0]
                if len(rsttexts) > 1:
                    item['rst2'] = rsttexts[1]
                if len(rsttexts) > 2:
                    item['rst3'] = rsttexts[2]
                #assign the content of the comment
                item['content'] = self.lsttostr(commentnode.select('div[@class="content"]/div[@class="comment-txt"]/div/text()').extract()).strip('\n').strip(' ')
                recommendnodes = commentnode.select('div[@class="content"]/div[@class="comment-recommend"]')
                for recommendnode in recommendnodes:
                    basenametext = recommendnode.select('text()').extract()[0].strip('\r\n').strip(' ')
                    extnamelst = recommendnode.select('a/text()').extract()
                    if u'推荐' in basenametext:
                        item['recPro'] = extnamelst
                    elif u'标签' in basenametext:
                        item['tags'] = extnamelst
                    elif u'喜欢' in basenametext:
                        item['favorate_Pro'] = extnamelst
                    elif u'特色' in basenametext:
                        item['specials'] = extnamelst
                    elif u'停车' in basenametext:
                        item['car_stop'] = extnamelst
                    elif u'氛围' in basenametext:
                        item['atmosphere'] = extnamelst
                    else:
                        pass
                item['time'] = self.lsttostr(commentnode.select('div[@class="content"]/div[@class="misc-info"]/span[@class="time"]/text()').extract())
                countnodes = commentnode.select('div[@class="content"]/div[@class="misc-info"]/span[@class="col-right"]/span')
                if len(countnodes) > 1:
                    zcountnode = countnodes[0].select('a/span[@class="heart-num"]/text()').extract()
                    if zcountnode:
                        item['zan_count'] = zcountnode[0].strip('(').strip(')').strip('\n').strip(' ')
                    rcountnode = countnodes[1].select('em[@class="col-exp"]/text()').extract()
                    if rcountnode:
                        item['reply_count'] = rcountnode[0].strip('\n').strip('(').strip(')').strip(' ')
                yield item
        else:
            #log.msg('==========+++++YelboshMessage+++++========Processing  '+str(response.url)+'........==========+++++YelboshMessage+++++==========')
            commentnodes = hxs.select('//div[@class="comment-list other-sign"]/ul/li')
            for commentnode in commentnodes:
                #initialize the item
                item = CommentItem()
                self.init_Item(item)
                item['path'] = response.meta['path']
                item['type'] = response.meta['type']
                item['username'] = self.lsttostr(commentnode.select('div[@class="pic"]/p[@class="name"]/a/text()').extract())
                connode = commentnode.select('div[@class="pic"]/p[@class="contribution"]/span')
                if connode:
                    item['usercontrib'] = self.lsttostr(connode.select('@class').extract())[-2:]
                item['time'] = self.lsttostr(commentnode.select('div[@class="content"]/div[@class="comment-txt"]/p[1]/span[@class="time"]/text()').extract())
                rankrstnode = commentnode.select('div[@class="content"]/div[@class="comment-txt"]/p/span[2]')
                if rankrstnode:
                    item['rankrst'] = self.lsttostr(rankrstnode.select('@class').extract())[-2:]
                item['content'] = self.lsttostr(commentnode.select('div[@class="content"]/div[@class="comment-txt"]/p[2]/text()').extract())
                yield item
        
        
        
        
        
        
        
        
        
        
        
        
