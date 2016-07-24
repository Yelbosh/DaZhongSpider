#-*- coding: UTF-8 -*-

import os
from scrapy import log
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from DaZhong.items import ShopItem, TuanListItem,RecDishItem

class CommonShopSpider(Spider):
    name = 'CommonShopSpider'

    def __init__(self, category=None, *args, **kwargs):
        super(CommonShopSpider, self).__init__(*args, **kwargs)
        self.basepath = "DaZhongData/Shops/"
        self.track = open('badlink.log','a')
        self.workpart = ['结婚']
        self.foreign = open('foreign','a')
        self.urlhead = 'http://www.dianping.com'
        #for test
        self.starturl = 'http://www.dianping.com/search/category/2/10/g311'

    def init_Item(self,item):
        item['id'] = ''
        item['bigclass'] = ''
        item['city'] = ''
        item['smallclass'] = ''
        item['name'] = ''
        item['rankrst'] = ''
        item['commentcount'] = ''
        item['average'] = ''
        item['rst1'] = ''
        item['rst2'] = ''
        item['rst3'] = ''
        item['area'] = ''
        item['address'] = ''
        item['call1'] = ''
        item['call2'] = ''
        item['character'] = ''
        item['time'] = ''
        item['tags'] = []
        item['payway'] = ''
        item['alias'] = ''
        item['desc'] = ''
        #list field
        item['recPro'] = []
        item['tuanlist'] = []

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
                path2 = path1 + '/' + city + '/index'
                if os.path.exists(path2):
                    indexfile = open(path2,'r')
                    for indexline in indexfile.readlines():
                        linestrs = indexline.strip('\n').split('\t')
                        if len(linestrs) == 2:
                            smallclass = linestrs[0]
                            scurl = linestrs[1]
                            if '频道' in smallclass:
                                pass
                            else:
                                #construct the Request and yield it !
                                realurl = self.urlhead + scurl
                                #arequest = Request(realurl,meta={'bigclass':'美食','city':'北京','smallclass':'北京菜'},callback=self.parse_test)
                                arequest = Request(realurl,meta={'bigclass':bigclass,'city':city,'smallclass':smallclass},callback=self.parse_pagelinks)
                                requests.append(arequest)
        return requests
##        arequest = Request(self.starturl,meta={'bigclass':'美食','city':'北京','smallclass':'北京菜'},callback=self.parse_test)
##        arequest = Request(self.starturl,meta={'bigclass':'美食','city':'北京','smallclass':'北京菜'},callback=self.parse_pagelinks)
##        requests.append(arequest)
##        return requests
    
    #it is responsible for the page links' extraction
    def parse_pagelinks(self,response):
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
                realurl = baseurl + 'p' + str(pageindex)
                #request = Request(realurl,meta=response.meta,callback=self.parse_test)
                request = Request(realurl,meta=response.meta,callback=self.parse_links)
                yield request
                pageindex = pageindex + 1
            except Exception , e:
                self.track.write(request.url+'\n')
                raise DropItem(str(e))
        pass
        
    #this callback is used for test
    def parse_test(self,response):
        log.msg('==========+++++YelboshMessage+++++========Processing  '+str(response.meta['bigclass'])+'........==========+++++YelboshMessage+++++==========')
        log.msg('==========+++++YelboshMessage+++++========Processing  '+str(response.url)+'........==========+++++YelboshMessage+++++==========')
        pass
    
    #it is responsible for the links' extraction
    def parse_links(self,response):
        hxs = HtmlXPathSelector(response)
        nodelist = hxs.select('//*[@id="searchList"]/dl/dd')
        for item in nodelist:
            urlend = item.select('ul[2]/li[1]/a[1]/@href').extract()
            if urlend:
                url = self.urlhead + urlend[0].encode('utf8')
                request = Request(url,meta=response.meta,callback=self.parse_items)
                yield request

    #it is responsible for the items' extraction
    def parse_items(self, response):
        #initialize the item
        item = ShopItem()
        self.init_Item(item)
        #the info of the dir
        item['bigclass'] = response.meta['bigclass']
        item['city'] = response.meta['city']
        item['smallclass'] = response.meta['smallclass']
        urlfracs = response.url.split('/')
        id = urlfracs[len(urlfracs)-1]
        #the selector
        hxs = HtmlXPathSelector(response)
        
        #assign the id of the item
        item['id'] = id
        
        #================Analyze the html====================
        mainNode = hxs.select('//div[@class="main"]')
        #assign the name of the item
        names = mainNode.select('div[1]/div[1]/div[@class="shop-tit"]/div[1]/h1/text()').extract()
        if names:
            item['name'] = self.lsttostr(names).strip('\r\n').strip(' ')
        #assign the rankrst of the item
        cmtinfoNode = mainNode.select('div[1]/div[1]/div[@class="shop-tit"]/div[2]')
        rankrsts = cmtinfoNode.select('span/text()').extract()
        if rankrsts:
            item['rankrst'] = self.lsttostr(rankrsts).strip('\r\n').strip(' ')
        #assign the commentcount of the item
        commentcounts = cmtinfoNode.select('div/a/em/text()').extract()
        if commentcounts:
            item['commentcount'] = self.lsttostr(commentcounts).strip('\r\n').strip(' ')
        #assign the average of the item
        spansGrades = cmtinfoNode.select('div/span/strong/text()').extract()
        if len(spansGrades) > 0:
            item['average'] = spansGrades[0].strip('\r\n').strip(' ')
        #assign the rankgrade of the item
        if len(spansGrades) > 1:
            item['rst1'] = spansGrades[1]
        if len(spansGrades) > 2:
            item['rst2'] = spansGrades[2]
        if len(spansGrades) > 3:
            item['rst3'] = spansGrades[3]
        
        #==============Detail Analyze the Html==============
        shopinfoNode = mainNode.select('div[1]/div[1]/div[@class="pic-txt"]/div[2]/div[@class="shop-info-location"]')
        #assign the basic info of the item
        baseinfoNodes = shopinfoNode.select('div[@class="shop-location"]/ul/li')
        for baseinfoNode in baseinfoNodes:
            basename = baseinfoNode.select('em/text()').extract()
            if basename:
                #assign the field of the item according to the basename
                basenametext = basename[0].strip('\r\n').strip(' ')
                if u'地址' in basenametext:
                    item['area'] = self.lsttostr(baseinfoNode.select('a/span/text()').extract()).strip('\r\n').strip(' ')
                    item['address'] = self.lsttostr(baseinfoNode.select('span/text()').extract()).strip('\r\n').strip(' ')
                elif u'电话' in basenametext:
                    calls = baseinfoNode.select('span/text()').extract()
                    if len(calls) > 0:
                        item['call1'] = calls[0].strip('\r\n').strip(' ')
                    if len(calls) > 1:
                        item['call2'] = calls[1]
                elif u'特色' in basenametext:
                    item['character'] = self.lsttostr(baseinfoNode.select('a/text()').extract()).strip('\r\n').strip(' ')
                #for extension
                else:
                    pass
        #==============Extension Analyze the Html==============
        extinfoNodes = hxs.select('//div[@class="desc-list Hide"]/ul/li')
        for extinfoNode in extinfoNodes:
            extname = extinfoNode.select('em/text()').extract()
            if extname:
                #assign the field of the item according to the extname
                extnametext = extname[0].strip('\r\n').strip(' ')
                if u'特色' in extnametext:
                    item['character'] =  self.lsttostr(extinfoNode.select('a/text()').extract()).strip('\r\n').strip(' ')
                elif u'时间' in extnametext:
                    item['time'] = self.lsttostr(extinfoNode.select('span/text()').extract()).strip('\r\n').strip(' ')
                elif u'付款' in extnametext:
                    item['payway'] = extinfoNode.select('text()').extract()[0].encode('utf8').strip('\r\n').strip(' ')
                elif u'标签' in extnametext:
                    item['tags'] = extinfoNode.select('div/span[@class="desc-tag"]/a/text()').extract()
                elif u'别名' in extnametext:
                    item['alias'] = extinfoNode.select('text()').extract()[1].encode('utf8').strip('\r\n').strip(' ')
                elif u'简介' in extnametext:
                    item['desc'] = extinfoNode.select('text()').extract()[1].encode('utf8').strip('\r\n').strip(' ')
                else:
                    pass
        #==================The deep info of this item=====================
        #assign the tuanlist of the item
        tuannodes = hxs.select('//div[@class="promo-info J_toggle"]/div[@id="promo-deal-container"]/ul/li')
        for tuannode in tuannodes:
            tuan = TuanListItem()
            tuan['price'] = self.lsttostr(tuannode.select('a/strong/text()').extract()).strip('\r\n').strip(' ')
            tuan['title'] = tuannode.select('a/text()').extract()[1].encode('utf8').strip('\r\n').strip(' ')
            tuan['desc'] = self.lsttostr(tuannode.select('a/span/text()').extract()).strip('\r\n').strip(' ')
            item['tuanlist'].append(tuan)
        #recPro list
        recPronodes = hxs.select('//div[@class="vegetable"]/ul/li[position()<last()]')
        for recPronode in recPronodes:
            dish = RecDishItem()
            dish['name'] = self.lsttostr(recPronode.select('a/text()').extract()).strip('\r\n').strip(' ')
            dish['count'] = self.lsttostr(recPronode.select('em/text()').extract()).strip('(').strip(')')
            item['recPro'].append(dish)
        #yield the request to crawl the default comments
        defaulturl = response.url + '/review_all'
        yield item
        pass

