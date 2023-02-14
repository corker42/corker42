# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:27:47 2022

@author: sanyuan
"""

import requests
from lxml import etree
import xlwt
import time

urls = ["https://www.ceic.ac.cn/speedsearch?time=6&&page={}".format(i) for i in range(1,61)]
headers = {
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        }
infos = []
url = urls[0]
requests.packages.urllib3.disable_warnings()
r = requests.get(url=url, headers=headers, verify=False)
r.encoding = r.apparent_encoding
r= r.text
html = etree.HTML(r)
html = etree.HTML(r)
hd = html.xpath("//table//tr//th/text()")
try:
    for url in urls:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url=url, headers=headers, verify=False)
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        r= r.text
        html = etree.HTML(r)
        html = etree.HTML(r)
        Magnitude = html.xpath("//table//tr//td[1]")
        Moment = html.xpath("//table//tr//td[2]")
        latitude = html.xpath("//table//tr//td[3]")
        longitude = html.xpath("//table//tr//td[4]") 
        depth = html.xpath("//table//tr//td[5]")
        MomReference_locationent = html.xpath("//table//tr//td[6]")
        for i in range(0,len(Magnitude)):
            info = {
                hd[0]:Magnitude[i].xpath("string(.)"),
                hd[1]:Moment[i].xpath("string(.)"),
                hd[2]:latitude[i].xpath("string(.)"),
                hd[3]:longitude[i].xpath("string(.)"),
                hd[4]:depth[i].xpath("string(.)"),
                hd[5]:MomReference_locationent[i].xpath("string(.)")
                }
            infos.append(info)
        print('下载完成!!!')
        time.sleep(2)
except:
    'continue'
workbook = xlwt.Workbook(encoding='utf8')
every_info = workbook.add_sheet('every_info')
keys =  list(infos[0].keys())
for i,key in zip(range(len(keys)),keys):
    every_info.write(0,i,key)
for row in range(1,len(infos)+1,1):
    for col,key in zip(range(len(keys)),keys):
        every_info.write(row,col,str(infos[row-1][key]))
workbook.save("地震数据.xls")
        













