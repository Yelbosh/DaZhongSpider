# Scrapy settings for DaZhong project

SPIDER_MODULES = ['DaZhong.spiders']
NEWSPIDER_MODULE = 'DaZhong.spiders'
DEFAULT_ITEM_CLASS = 'DaZhong.items.CityItem'

USER_AGENT_LIST = [
    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)',
    'Mozilla/5.0 (compatible; iaskspider/1.0; MSIE 6.0)',
    'Sogou web spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)',
    'Mozilla/5.0 (compatible; YodaoBot/1.0;http://www.yodao.com/help/webmaster/spider/;)',
    'msnbot/1.0 (+http://search.msn.com/msnbot.htm)',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'
]
DOWNLOADER_MIDDLEWARES = {
##    'DaZhong.RetryProxyMiddleware.RetryProxyMiddleware': 500,
##    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
##    'DaZhong.ProxyMiddleware.ProxyMiddleware': 750,
##    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'DaZhong.RandomUserAgentMiddleware.RandomUserAgentMiddleware':400,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None
}


##PROXY_LIST = open('./proxy.txt','r').readlines()

RETRY_ENABLED = True
RETRY_TIMES = 5

DOWNLOAD_DELAY = 0.5    # 500 ms of delay
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False

##ITEM_PIPELINES = ['DaZhong.FilterCommonShopItemsPipeline.FilterCommonShopItemsPipeline']
#ITEM_PIPELINES = ['DaZhong.pipelines.FilterCityItemsPipeline']
ITEM_PIPELINES = ['DaZhong.pipelines.ProxyPipeline']
#ITEM_PIPELINES = ['DaZhong.FilterCommentItemsPipeline.FilterCommentItemsPipeline']

##LOG_ENABLED = True
##LOG_ENCODING = 'utf-8'
##LOG_FILE = './commonshop.log'
##LOG_LEVEL = 'DEBUG'
##LOG_STDOUT = False
