# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/28
# @Author : Owen

"""
需求人：黄思颖
需求：提取附件中号码，合并后去重。
"""
import pandas as pd
import os

os.chdir(r'C:\Users\Administrator\Desktop\中间号')
os.chdir(r'D:\中移互联网\财务审计\【3】收集的资料\是否为行业应用卡')
file_list = os.listdir()
file_list = [x for x in file_list if '.gz' not in x]

data = []

for file in file_list:

    print('正在处理：{file_name}'.format(file_name=file))
    chunk_tmp = pd.read_csv(file, header=None, usecols=[1], names=['mobileno'], sep='|',
                            chunksize=1000000, dtype='str')

    for chunk in chunk_tmp:
        chunk = chunk.drop_duplicates()
        data.append(chunk)

data = pd.concat(data, ignore_index=True)
data = data.drop_duplicates()

data.to_csv(r'和多号中间号主叫号码清单（全量）.txt', index=False)
data = pd.read_csv(r'和多号中间号主叫号码清单（全量）.txt', dtype='str')

tmp = data.loc[data.mobileno.map(lambda x: len(str(x)) != 11)]
tmp.to_csv(r'和多号中间号主叫号码清单（非手机号）.txt', index=False)

tmp = data.loc[data.mobileno.map(lambda x: str(x).startswith('1') and len(str(x)) == 11)]
tmp.to_csv(r'和多号中间号主叫号码清单（手机号）.txt', index=False)
tmp = pd.read_csv(r'和多号中间号主叫号码清单（手机号）.txt', dtype='str')
tmp['tag'] = 1
tmp[['tag', 'mobileno']].to_csv(r'和多号中间号主叫号码清单（手机号）-tag.txt', index=False)
