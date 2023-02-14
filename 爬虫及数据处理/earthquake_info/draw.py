# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:31:56 2022

@author: sanyuan
"""

import xlrd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import os

workbook = xlrd.open_workbook('四川地震数据.xls')
a = workbook.sheet_names()
infos = workbook.sheet_by_name(a[0])
rows = infos.nrows
cols = infos.ncols
hd = infos.row_values(0)
Magnitude = infos.col_values(0)
locationent = infos.col_values(5)


c = (
    Map()
    .add("四川", [list(z) for z in zip(locationent, Magnitude)], "四川")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="四川地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render()
)
os.system("render.html")






