# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/14
# @Author : Owen

"""
需求人：黄媛
需求：财务收支类审计，合并单个excel中所有sheet，仅保留指定字段。
"""

import pandas as pd
import os

path = r'C:\Users\Administrator\Desktop'
os.chdir(path)
file = r'汇总所有应收账款.xlsx'

sheet_list = pd.ExcelFile(file).sheet_names

data = []

for sheet in sheet_list:

    print('正在处理：{sheet_name}'.format(sheet_name=sheet))

    tmp = pd.read_excel(file, sheet_name=sheet)
    tmp = tmp[['列账月份', '所属业务', '公司', '金额']]

    data.append(tmp)

data = pd.concat(data, ignore_index=True)
data.drop_duplicates(inplace=True)

data.to_excel(r'汇总所有应收账款（合并）.xlsx', index=False)
