# -*- coding:utf-8 -*-

from scrapy import log
from DaZhong.settings import PROXY_LIST
import random

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        item   = random.choice(PROXY_LIST)
        arr    = item.split('\t')
        #log.msg('===================the proxy ip is ==================='+arr[0]+'======================================')
        request.meta['proxy'] = 'http://%s:%s' % (arr[0],arr[1])