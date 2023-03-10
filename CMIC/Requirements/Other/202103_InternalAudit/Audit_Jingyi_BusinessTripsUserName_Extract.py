# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/12
# @Author : Owen

"""
需求人：杨静宜
需求：财务收支类审计，从“事由及说明”字段中，提取出出差人姓名。
"""

import pandas as pd
import os
import re

os.chdir(r'C:\Users\Administrator\Desktop')
data = pd.read_excel(r'差旅费201901-202005.xlsx')

s = '付周汉超、赵晓静、李剑苹、陈珊、秦丹娜、黄颖办出差（洛阳）差旅费（P190101083）'
pattern = re.compile(r'.*?付(.*)办出差')
gp = re.search(pattern, str(s))
gp.group(0)
gp.group(1)
gp.group(2)

def extract_name(s):
    pattern = re.compile(r'.*?付(.*)办出差')
    gp = re.search(pattern, str(s))
    if gp:
        return gp.group(1)
    else:
        return 'else'

data['出差人'] = data['事由及说明'].map(extract_name)

data.to_excel(r'差旅费201901-202005（匹配后）.xlsx')
