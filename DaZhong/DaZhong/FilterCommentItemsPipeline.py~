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

class FilterCommentItemsPipeline(object):
    def __init__(self):
        self.basepath = './DaZhongData/Shops/'
        self.logfile = open('./commentshoppipeline.log','a')
        pass
        
    def process_item(self, item, spider):
        path = item['path']
        type = item['type']
        #path = self.basepath + item['bigclass'] + '/' + item['city'] + '/' + item['smallclass'] + '/' + item['id']
        try:
            if os.path.exists(path) is False:
                os.makedirs(path)
            else:
                pass
            if type is not 'short':
                id = len(os.listdir(path)) + 1
                file = open(path+'/'+str(id)+'.xml','w')
                #construct the xml files
                doc = Document()
                #base info
                if type is 'default':
                    baseNode = doc.createElement('defaultcomment')
                else:
                    baseNode = doc.createElement('tuancomment')
                baseNode.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")#设置命名空间
                doc.appendChild(baseNode)
                #====     append the username node    ====
                namenode = doc.createElement('username')
                namenode.appendChild(doc.createTextNode(item['username']))
                baseNode.appendChild(namenode)
                #====     append the contribution node    ====
                contributionnode = doc.createElement('usercontrib')
                contributionnode.appendChild(doc.createTextNode(item['usercontrib']))
                baseNode.appendChild(contributionnode)
                #====     append the rankrst node    ====
                rankrstnode = doc.createElement('rankrst')
                rankrstnode.appendChild(doc.createTextNode(item['rankrst']))
                baseNode.appendChild(rankrstnode)
                #====     append the average node    ====
                averagenode = doc.createElement('average')
                averagenode.appendChild(doc.createTextNode(item['average']))
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
                #====     append the content node    ====
                contentnode = doc.createElement('content')
                contentnode.appendChild(doc.createTextNode(item['content']))
                baseNode.appendChild(contentnode)
                #====     append the recPro    ====
                dishlistnode = doc.createElement('recommend-dish-list')
                for dishname in item['recPro']:
                    dishnode = doc.createElement('dish')
                    dishnode.appendChild(doc.createTextNode(dishname.encode('utf8')))
                    dishlistnode.appendChild(dishnode)
                baseNode.appendChild(dishlistnode)
                #====     append the tags node    ====
                tagsnode = doc.createElement('tags')
                for tag in item['tags']:
                    tagnode = doc.createElement('tag')
                    tagnode.appendChild(doc.createTextNode(tag.encode('utf8')))
                    tagsnode.appendChild(tagnode)
                baseNode.appendChild(tagsnode)
                #====     append the favorate_Pro node    ====
                favorate_Pronodes = doc.createElement('favorate-dish-list')
                for favorate_Pronode in item['favorate_Pro']:
                    favoratenode = doc.createElement('dish')
                    favoratenode.appendChild(doc.createTextNode(favorate_Pronode.encode('utf8')))
                    favorate_Pronodes.appendChild(favoratenode)
                baseNode.appendChild(favorate_Pronodes)
                #====     append the specials node    ====
                specialsnode = doc.createElement('special-list')
                for special in item['specials']:
                    specialnode = doc.createElement('special')
                    specialnode.appendChild(doc.createTextNode(special.encode('utf8')))
                    specialsnode.appendChild(specialnode)
                baseNode.appendChild(specialsnode)
                #====     append the carsstop node    ====
                carsnode = doc.createElement('car-stop-info')
                for car in item['car_stop']:
                    carnode = doc.createElement('carstop')
                    carnode.appendChild(doc.createTextNode(car.encode('utf8')))
                    carsnode.appendChild(carnode)
                baseNode.appendChild(carsnode)
                #====     append the atmosphere node    ====
                atmospheresnode = doc.createElement('atmosphere-list')
                for atmosphere in item['atmosphere']:
                    atmospherenode = doc.createElement('atmosphere')
                    atmospherenode.appendChild(doc.createTextNode(atmosphere.encode('utf8')))
                    atmospheresnode.appendChild(atmospherenode)
                baseNode.appendChild(atmospheresnode)
                #====     append the time node    ====
                timenode = doc.createElement('time')
                timenode.appendChild(doc.createTextNode(item['time']))
                baseNode.appendChild(timenode)
                #====     append the zan_count node    ====
                zannode = doc.createElement('zan_count')
                zannode.appendChild(doc.createTextNode(item['zan_count'].encode('utf8')))
                baseNode.appendChild(zannode)
                #====     append the reply_count node    ====
                replynode = doc.createElement('reply_count')
                replynode.appendChild(doc.createTextNode(item['reply_count'].encode('utf8')))
                baseNode.appendChild(replynode)
                
                #write the xml to document
                file.write(doc.toprettyxml(indent="    "))
                file.flush()
                file.close()
            else:
                id = len(os.listdir(path)) + 1
                file = open(path+'/'+str(id)+'.xml','w')
                #construct the xml files
                doc = Document()
                #base info
                baseNode = doc.createElement('shortcomment')
                baseNode.setAttribute('xmlns:xsi',"http://www.w3.org/2001/XMLSchema-instance")#设置命名空间
                doc.appendChild(baseNode)
                #====     append the username node    ====
                namenode = doc.createElement('username')
                namenode.appendChild(doc.createTextNode(item['username']))
                baseNode.appendChild(namenode)
                #====     append the contribution node    ====
                contributionnode = doc.createElement('usercontrib')
                contributionnode.appendChild(doc.createTextNode(item['usercontrib']))
                baseNode.appendChild(contributionnode)
                #====     append the rankrst node    ====
                rankrstnode = doc.createElement('rankrst')
                rankrstnode.appendChild(doc.createTextNode(item['rankrst']))
                baseNode.appendChild(rankrstnode)
                #====     append the content node    ====
                contentnode = doc.createElement('content')
                contentnode.appendChild(doc.createTextNode(item['content']))
                baseNode.appendChild(contentnode)
                #====     append the time node    ====
                timenode = doc.createElement('time')
                timenode.appendChild(doc.createTextNode(item['time']))
                baseNode.appendChild(timenode)
                
                #write the xml to document
                file.write(doc.toprettyxml(indent="    "))
                file.flush()
                file.close()
        except Exception , e:
            raise DropItem(str(e))
            file.flush()
            file.close()
            self.logfile.write(time.strftime("%H:%M:%S") + '\t' + str(e) + '\n')
