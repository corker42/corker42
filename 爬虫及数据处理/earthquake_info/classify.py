# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:37:16 2022

@author: sanyuan
"""

import xlwt
import xlrd

workbook = xlrd.open_workbook('地震数据.xls')
a = workbook.sheet_names()
infos = workbook.sheet_by_name(a[0])
rows = infos.nrows
cols = infos.ncols
hd = infos.row_values(0)
info = []
try:
    for i in range(rows+1):
        if "四川" in infos.cell_value(i,5):
            info.append(infos.row_values(i))
except:
    print('0')

sc_info = []
for i in range(len(info)):
    dic = {
        hd[0]:info[i][0],
        hd[1]:info[i][1],
        hd[2]:info[i][2],
        hd[3]:info[i][3],
        hd[4]:info[i][4],
        hd[5]:info[i][5]
        }
    sc_info.append(dic)
workbook = xlwt.Workbook(encoding='utf8')
sichuan_info = workbook.add_sheet('sichuan_info')
keys =  list(sc_info[0].keys())
for i,key in zip(range(len(keys)),keys):
    sichuan_info.write(0,i,key)
for row in range(1,len(sc_info)+1,1):
    for col,key in zip(range(len(keys)),keys):
        sichuan_info.write(row,col,str(sc_info[row-1][key]))
workbook.save("四川地震数据.xls")
