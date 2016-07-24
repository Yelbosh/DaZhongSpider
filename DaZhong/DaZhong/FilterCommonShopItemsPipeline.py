# -*- coding:utf-8 -*-

import tools
from scrapy.exceptions import DropItem
import re
import urllib
import time
import exceptions
import socket
from scrapy import log
import os
from xml.dom.minidom import Document

class FilterCommonShopItemsPipeline(object):
    def __init__(self):
        self.basepath = '/media/D3D801CC0352E222/1/'
        self.logfile = open('./commonshoppipeline.log','a')
        pass
    
    def process_item(self, item, spider):
        path = self.basepath + item['bigclass'] + '/' + item['city'] + '/' + item['smallclass'] + '/' + item['id']
        try:
            if os.path.exists(path) is False:
                os.makedirs(path)
            else:
                pass
            if True:
                file = open(path+'/'+item['id']+'_base.xml','w')
                #construct the xml files
                doc = Document()
                #base info
                baseNode = doc.createElement('shopinfo')
                baseNode.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")#设置命名空间
                doc.appendChild(baseNode)
                #====     append the id node    ====
                idnode = doc.createElement('id')
                idnode.appendChild(doc.createTextNode(item['id']))
                baseNode.appendChild(idnode)
                #====     append the bigclass node    ====
                bigclassnode = doc.createElement('bigclass')
                bigclassnode.appendChild(doc.createTextNode(item['bigclass']))
                baseNode.appendChild(bigclassnode)
                #====     append the city node    ====
                citynode = doc.createElement('city')
                citynode.appendChild(doc.createTextNode(item['city']))
                baseNode.appendChild(citynode)
                #====     append the smallclass node    ====
                smallclassnode = doc.createElement('smallclass')
                smallclassnode.appendChild(doc.createTextNode(item['smallclass']))
                baseNode.appendChild(smallclassnode)
                #====     append the name node    ====
                namenode = doc.createElement('name')
                namenode.appendChild(doc.createTextNode(item['name']))
                baseNode.appendChild(namenode)
                #====     append the rankrst node    ====
                rankrstnode = doc.createElement('rankrst')
                rankrstnode.appendChild(doc.createTextNode(item['rankrst']))
                baseNode.appendChild(rankrstnode)
                #====     append the commentcount node    ====
                commentcountnode = doc.createElement('commentcount')
                commentcountnode.appendChild(doc.createTextNode(item['commentcount']))
                baseNode.appendChild(commentcountnode)
                #====     append the average node    ====
                averagenode = doc.createElement('average')
                averagenode.appendChild(doc.createTextNode(item['average'].encode('utf8')))
                baseNode.appendChild(averagenode)
                #====     append the rst1 node    ====
                rst1node = doc.createElement('rst1')
                rst1node.appendChild(doc.createTextNode(item['rst1'].encode('utf8')))
                baseNode.appendChild(rst1node)
                #====     append the rst2 node    ====
                rst2node = doc.createElement('rst2')
                rst2node.appendChild(doc.createTextNode(item['rst2'].encode('utf8')))
                baseNode.appendChild(rst2node)
                #====     append the rst3 node    ====
                rst3node = doc.createElement('rst3')
                rst3node.appendChild(doc.createTextNode(item['rst3'].encode('utf8')))
                baseNode.appendChild(rst3node)
                #====     append the area node    ====
                areanode = doc.createElement('area')
                areanode.appendChild(doc.createTextNode(item['area']))
                baseNode.appendChild(areanode)
                #====     append the address node    ====
                addressnode = doc.createElement('address')
                addressnode.appendChild(doc.createTextNode(item['address']))
                baseNode.appendChild(addressnode)
                #====     append the calls node    ====
                callsnode = doc.createElement('calls')
                if item['call1']:
                    call1node = doc.createElement('call')
                    call1node.appendChild(doc.createTextNode(item['call1'].encode('utf8')))
                    callsnode.appendChild(call1node)
                if item['call2']:
                    call2node = doc.createElement('call')
                    call2node.appendChild(doc.createTextNode(item['call2'].encode('utf8')))
                    callsnode.appendChild(call2node)
                baseNode.appendChild(callsnode)
                #====     append the character node    ====
                characternode = doc.createElement('character')
                characternode.appendChild(doc.createTextNode(item['character']))
                baseNode.appendChild(characternode)
                #====     append the time node    ====
                timenode = doc.createElement('time')
                timenode.appendChild(doc.createTextNode(item['time']))
                baseNode.appendChild(timenode)
                #====     append the payway node    ====
                paywaynode = doc.createElement('payway')
                paywaynode.appendChild(doc.createTextNode(item['payway']))
                baseNode.appendChild(paywaynode)
                #====     append the tags node    ====
                tagsnode = doc.createElement('tags')
                for tag in item['tags']:
                    tagnode = doc.createElement('tag')
                    tagnode.appendChild(doc.createTextNode(tag.encode('utf8')))
                    tagsnode.appendChild(tagnode)
                baseNode.appendChild(tagsnode)
                #====     append the alias node    ====
                aliasnode = doc.createElement('alias')
                aliasnode.appendChild(doc.createTextNode(item['alias']))
                baseNode.appendChild(aliasnode)
                #====     append the desc node    ====
                descnode = doc.createElement('desc')
                descnode.appendChild(doc.createTextNode(item['desc']))
                baseNode.appendChild(descnode)
                #====     append the tuanlist    ====
                tuanlistnode = doc.createElement('tuanlist')
                for tuanitem in item['tuanlist']:
                    tuannode = doc.createElement('tuan')
                    #tuan title
                    tuantitle = doc.createElement('title')
                    tuantitle.appendChild(doc.createTextNode(tuanitem['title']))
                    tuannode.appendChild(tuantitle)
                    #tuan price
                    tuanprice = doc.createElement('price')
                    tuanprice.appendChild(doc.createTextNode(tuanitem['price']))
                    tuannode.appendChild(tuanprice)
                    #tuan desc
                    tuandesc = doc.createElement('desc')
                    tuandesc.appendChild(doc.createTextNode(tuanitem['desc']))
                    tuannode.appendChild(tuandesc)
                    #append
                    tuanlistnode.appendChild(tuannode)
                baseNode.appendChild(tuanlistnode)
                #====     append the recPro    ====
                dishlistnode = doc.createElement('dishlist')
                for dishitem in item['recPro']:
                    dishnode = doc.createElement('dish')
                    #dish name
                    dishname = doc.createElement('name')
                    dishname.appendChild(doc.createTextNode(dishitem['name']))
                    dishnode.appendChild(dishname)
                    #dish count
                    dishcount = doc.createElement('count')
                    dishcount.appendChild(doc.createTextNode(dishitem['count']))
                    dishnode.appendChild(dishcount)
                    #append
                    dishlistnode.appendChild(dishnode)
                baseNode.appendChild(dishlistnode)
                
                #write the xml to document
                file.write(doc.toprettyxml(indent="    "))
                
                #for the comment list fields
        except Exception , e:
            raise DropItem(str(e))
            self.logfile.write(time.strftime("%H:%M:%S") + '\t' + str(e) + '\t' + item['id'] + '\n')
