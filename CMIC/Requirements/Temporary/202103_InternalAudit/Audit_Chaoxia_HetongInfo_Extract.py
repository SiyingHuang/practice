# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/7
# @Author : Owen

"""
需求人：朱超霞
需求：财务收支类审计，需提取“行说明”字段中的合同名称、合同编号，增至列末尾。
"""

import pandas as pd
import os
import re

os.chdir(r'C:\Users\Administrator\Desktop')
exfile_name = '业务支撑费明细账'

data = pd.read_excel(exfile_name + r'.xlsx', sheet_name='2019年', skiprows=5, dtype='str')  # 该sheet已包含前两个sheet”

data = pd.read_excel(exfile_name + r'.xlsx', sheet_name='2020年6-12月', skiprows=1, dtype='str')  # 该sheet已包含前两个sheet”

s = '预列卓望数码技术（深圳）有限公司2017-2018年负一屏垂直应用技术支撑项目合同（标段2：IT类应用）CMIC-20180047进度款P170915166'
pattern = re.compile(r'.*公司(.*)(CMIC[0-9, \-]*)')
gp = re.search(pattern, str(s))
gp.group(0)
gp.group(1)
gp.group(2)

def extract_contract_name(s):
    pattern = re.compile(r'.*公司(.*)(CMIC[0-9, \-]*)')
    gp = re.search(pattern, str(s))
    if gp:
        return gp.group(1)
    else:
        return 'else'

def extract_contract_no(s):
    pattern = re.compile(r'.*?(CMIC-[0-9, \-]*)')
    gp = re.search(pattern, str(s))
    if gp:
        return gp.group(1)
    else:
        return 'else'

data['合同名称'] = data['行说明'].map(extract_contract_name)
data['合同编号'] = data['行说明'].map(extract_contract_no)
data.info()

data.to_excel(r'业务支撑费明细账（处理后）.xlsx', index=False, sheet_name='前两个sheet')
data.to_excel(r'业务支撑费明细账2（处理后）.xlsx', index=False, sheet_name='后两个sheet')
