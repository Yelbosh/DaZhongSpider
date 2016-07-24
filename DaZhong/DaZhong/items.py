# -*- coding:utf-8 -*-

from scrapy.item import Item, Field

class CityItem(Item):
    id = Field()
    name = Field()
    url = Field()
    pass
    
class ShopItem(Item):
    id = Field()
    bigclass = Field()
    city = Field()
    smallclass = Field()
    name = Field()
    rankrst = Field()#星级排名
    commentcount = Field()
    average = Field()#人均
    rst1 = Field()#1：口味 2：效果 3：产品
    rst2 = Field()#环境
    rst3 = Field()#服务
    area = Field()#区
    address = Field()
    call1 = Field()#电话1
    call2 = Field()#电话2
    character = Field()#特色
    time = Field()#营业时间
    tags = Field()#标签
    payway = Field()#付款方式
    alias = Field()#商户别名
    desc = Field()#商户简介
    recPro = Field()#推荐产品
    tuanlist = Field()#团购url列表
    pass

class TuanListItem(Item):
    price = Field()#价格
    title = Field()#名称
    desc = Field()#描述
    pass
    
#推荐菜item
class RecDishItem(Item):
    name = Field()
    count = Field()
    pass

#代理Item
class ProxyItem(Item):
    address   = Field()
    port      = Field()
    protocol  = Field()
    location  = Field()
    type      = Field()
    pass
    
#团购评论及其默认评论
class CommentItem(Item):
    path = Field()#保存路径
    type = Field()#类型
    username = Field()#用户名
    usercontrib = Field()#用户贡献
    rankrst = Field()#星级排名
    average = Field()#人均
    rst1 = Field()#1：口味 2：效果 3：产品
    rst2 = Field()#环境
    rst3 = Field()#服务
    content = Field()#评论内容
    recPro = Field()#推荐产品
    tags = Field()#标签
    favorate_Pro = Field()#喜欢的产品
    specials = Field()#特色
    car_stop = Field()#停车信息
    atmosphere = Field()#氛围
    time = Field()#时间
    zan_count = Field()#赞总数
    reply_count = Field()#回复总数
    pass
    
#短评论
class ShortCommentItem(Item):
    path = Field()#保存路径
    username = Field()#用户名
    usercontrib = Field()#用户贡献
    rankrst = Field()#星级排名
    content = Field()#评论内容
    time = Field()#时间
    pass

















