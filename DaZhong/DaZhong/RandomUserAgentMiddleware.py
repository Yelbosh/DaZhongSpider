# -*- coding:utf-8 -*-

import random
from DaZhong.settings import USER_AGENT_LIST
from scrapy import log

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(USER_AGENT_LIST)
        if ua:
            #log.msg('===================the random user-agent is ==================='+ua+'======================================')
            request.headers.setdefault('User-Agent', ua)