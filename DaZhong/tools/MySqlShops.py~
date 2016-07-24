#-*- coding: UTF-8 -*-
import MySQLdb
import os
from xml.dom import minidom  


def parse_xml_to_MySQL(path,cursor):
    id_value = ''
    bigclass_value = ''
    city_value = ''
    smallclass_value = ''
    name_value = ''
    rankrst_value = ''
    commentcount_value = ''
    average_value = ''
    rst1_value = ''
    rst2_value = ''
    rst3_value = ''
    area_value = ''
    address_value = ''
    call1_value = ''
    call2_value = ''
    character_value = ''
    time_value = ''
    tags_value = ''
    payway_value = ''
    alias_value = ''
    desc_value = ''
    #list field
    recPro_value = ''
    tuanlist_value = ''

    doc = minidom.parse(path)
    root = doc.documentElement
    ids = root.getElementsByTagName("id")
    if ids:
        if ids[0].childNodes:
            id_value = ids[0].childNodes[0].nodeValue
            #print id_value
    bigclasses = root.getElementsByTagName("bigclass")
    if bigclasses:
        if bigclasses[0].childNodes:
            bigclass_value = bigclasses[0].childNodes[0].nodeValue
            #print bigclass_value
    citys = root.getElementsByTagName("city")
    if citys:
        if citys[0].childNodes:
            city_value = citys[0].childNodes[0].nodeValue
            # print city_value
    smallclasses = root.getElementsByTagName("smallclass")
    if smallclasses:
        if smallclasses[0].childNodes:
            smallclass_value = smallclasses[0].childNodes[0].nodeValue
            #print smallclass_value
    names = root.getElementsByTagName("name")
    if  names:
        if names[0].childNodes:
            name_value = names[0].childNodes[0].nodeValue
            #print name_value
    rankrsts = root.getElementsByTagName("rankrst")
    if  rankrsts:
        if rankrsts[0].childNodes:
            rankrst_value = rankrsts[0].childNodes[0].nodeValue
            #print rankrst_value
    commentcounts = root.getElementsByTagName("commentcount")
    if  commentcounts:
        if commentcounts[0].childNodes:
            commentcount_value = commentcounts[0].childNodes[0].nodeValue
            #print commentcount_value
    averages = root.getElementsByTagName("average")
    if  averages:
        if averages[0].childNodes:
            average_value = averages[0].childNodes[0].nodeValue.strip('\n')
            #print average_value
    rst1s = root.getElementsByTagName("rst1")
    if  rst1s:
        if rst1s[0].childNodes:
            rst1_value = rst1s[0].childNodes[0].nodeValue
            #print rst1_value
    rst2s = root.getElementsByTagName("rst2")
    if  rst2s:
        if rst2s[0].childNodes:
            rst2_value = rst2s[0].childNodes[0].nodeValue
            #print rst2_value
    rst3s = root.getElementsByTagName("rst3")
    if  rst3s:
        if rst3s[0].childNodes:
            rst3_value = rst3s[0].childNodes[0].nodeValue
            #print rst3_value
    areas = root.getElementsByTagName("area")
    if areas:
        if areas[0].childNodes:
            area_value = areas[0].childNodes[0].nodeValue
            #print area_value
    addresss = root.getElementsByTagName("address")
    if addresss:
        if addresss[0].childNodes:
            address_value = addresss[0].childNodes[0].nodeValue.strip('\n')
            #print address_value
    #for the calls
    callsnode = root.getElementsByTagName("calls")
    if callsnode:
        calls = callsnode[0].getElementsByTagName("call")
        if calls:
            if calls[0].childNodes:
                call1_value = calls[0].childNodes[0].nodeValue
                #print call1_value
                if len(calls) > 1:
                    if calls[1].childNodes:
                        call2_value = calls[1].childNodes[0].nodeValue
                        #print call2_value
    characters = root.getElementsByTagName("character")
    if characters:
        if characters[0].childNodes:
            character_value = characters[0].childNodes[0].nodeValue
            #print character_value
    times = root.getElementsByTagName("time")
    if times:
        if times[0].childNodes:
            time_value = times[0].childNodes[0].nodeValue
            #print time_value
    #for the tags
    tagsnode = root.getElementsByTagName("tags")
    if tagsnode:
        tags = tagsnode[0].getElementsByTagName("tag")
        if tags:
            for tag in tags:
                if tag.childNodes:
                    tags_value = tags_value + tag.childNodes[0].nodeValue
                    if tag is not tags[len(tags)-1]:
                        tags_value = tags_value + '#'
            #print tags_value
    payways = root.getElementsByTagName("payway")
    if payways:
        if payways[0].childNodes:
            payway_value = payways[0].childNodes[0].nodeValue
            #print payway_value
    aliass = root.getElementsByTagName("alias")
    if aliass:
        if aliass[0].childNodes:
            alias_value = aliass[0].childNodes[0].nodeValue
            #print alias_value
    descs = root.getElementsByTagName("desc")
    if descs:
        if descs[0].childNodes:
            desc_value = descs[0].childNodes[0].nodeValue
            #print desc_value
    #for the recpro
    dishlistnode = root.getElementsByTagName("dishlist")
    if dishlistnode:
        dishs = dishlistnode[0].getElementsByTagName("dish")
        if dishs:
            for dish in dishs:
                dishnamenode = dish.getElementsByTagName("name")
                if dishnamenode:
                    dishname = dishnamenode[0]
                    if dishname.childNodes:
                        recPro_value = recPro_value + dishname.childNodes[0].nodeValue
                        recPro_value = recPro_value + '-'
                dishcountnode = dish.getElementsByTagName("count")
                if dishcountnode:
                    dishcount = dishcountnode[0]
                    if dishcount.childNodes:
                        recPro_value = recPro_value + dishcount.childNodes[0].nodeValue
                        if dish is not dishs[len(dishs)-1]:
                            recPro_value = recPro_value + '#'
            #print recPro_value
    #for the tuanlist
    tuanlistnode = root.getElementsByTagName("tuanlist")
    if tuanlistnode:
        tuans = tuanlistnode[0].getElementsByTagName("tuan")
        if tuans:
            for tuan in tuans:
                tuantitlenode = tuan.getElementsByTagName("title")
                if tuantitlenode:
                    tuantitle = tuantitlenode[0]
                    if tuantitle.childNodes:
                        tuanlist_value = tuanlist_value + tuantitle.childNodes[0].nodeValue
                        tuanlist_value = tuanlist_value + '-'
                tuanpricenode = tuan.getElementsByTagName("price")
                if tuanpricenode:
                    tuanprice = tuanpricenode[0]
                    if tuanprice.childNodes:
                        tuanlist_value = tuanlist_value + tuanprice.childNodes[0].nodeValue
                        tuanlist_value = tuanlist_value + '-'
                tuandescnode = tuan.getElementsByTagName("desc")
                if tuandescnode:
                    tuandesc = tuandescnode[0]
                    if tuandesc.childNodes:
                        tuanlist_value = tuanlist_value + tuandesc.childNodes[0].nodeValue
                        if tuan is not tuans[len(tuans)-1]:
                            tuanlist_value = tuanlist_value + '#'
            #print tuanlist_value
    sql = "insert into Shop (id,bigclass,city,smallclass,name,rankrst,commentcount,average,rst1,rst2,rst3,area,address,call1,call2,specials,time,payway,tags,alias,shopdesc,tuanlist,dishlist) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    try:
        cursor.execute(sql%(id_value,bigclass_value,city_value,smallclass_value,name_value,rankrst_value,commentcount_value,average_value,rst1_value,rst2_value,rst3_value,area_value,address_value,call1_value,call2_value,character_value,time_value,payway_value,tags_value,alias_value,desc_value,tuanlist_value,recPro_value))
        db.commit()
    except Exception , e:
        db.rollback()
        print e
    db.close

db = MySQLdb.connect("localhost","root","731987620","DaZhong",charset="utf8")
dbcursor = db.cursor()
path0 = '/media/D3D801CC0352E222/1'
workpart = ['结婚']
for bigclass in workpart:
            #get the citydirs of this bigclass
            path1 = path0 + '/' + bigclass
            citydirs = os.listdir(path1)
            for city in citydirs:
                #get the index file and yield the requests according to it
                path2 = path1 + '/' + city
                smallclasses = os.listdir(path2)
                for smallclass in smallclasses:
##                    if smallclass == '美容':
##                        smallclass = '美容/SPA'
                    #elif smallclass == '办公':
                    #   smallclass = '办公/文化用品'
                    path3 = path2 + '/' + smallclass
                    if os.path.isdir(path3):
                        items = os.listdir(path3)
                        for item in items:
                            path4 = path3 + '/' + item
                            if os.path.isdir(path4):
                                path5 = path4 + '/' + item + '_base.xml'
                                if os.path.exists(path5):
                                    #parse the xml file and store the field into the mysql database
                                    print '正在处理' + path5 + '……………………'
                                    try:
                                        parse_xml_to_MySQL(path5,dbcursor)
                                    except Exception , e:
                                        print '发生错误！文件可能为空！'
                                        print e
