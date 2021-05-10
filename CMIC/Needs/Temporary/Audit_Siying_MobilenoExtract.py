# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/28
# @Author : Owen

"""
需求人：黄思颖
需求：
    1、提取附件中号码，合并后去重；
    2、根据物联网卡号段，筛选符合要求号码。
"""
import pandas as pd
import os


# 一、和多号中间号
os.chdir(r'D:\中移互联网\财务审计\【3】收集的资料\是否为行业应用卡\和多号')
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


# 通过号段初步判别是否为物联网行业卡
# 1、采用以144、10647、10648开头的13位物联网专用号段
tmp = data.loc[data.mobileno.map(
    lambda x: (len(str(x)) == 13 and (
            str(x)[:3] == '144' or str(x)[:5] == '10647' or str(x)[:5] == '10648')))]

# 2、采用 1476、1724、1789、1849 开头的11位物联网专用号段
tmp = data.loc[data.mobileno.map(
    lambda x: (len(str(x)) == 11 and (
                str(x)[:4] == '1476' or str(x)[:4] == '1724' or str(x)[:4] == '1789' or str(x)[:4] == '1849')))]

# 3、满足1或2的条件
tmp = data.loc[data.mobileno.map(
    lambda x: ((len(str(x)) == 13 and (
            str(x)[:3] == '144' or str(x)[:5] == '10647' or str(x)[:5] == '10648')) or
              (len(str(x)) == 11 and (
            str(x)[:4] == '1476' or str(x)[:4] == '1724' or str(x)[:4] == '1789' or str(x)[:4] == '1849'))))]

tmp.to_csv(r'和多号中间号主叫号码清单（已匹配物联网号段）.txt', index=False)



# 二、龙江会员
os.chdir(r'D:\中移互联网\财务审计\【3】收集的资料\是否为行业应用卡\龙江会员')
file = '龙江会员订购数据-对账文件.txt'

data = pd.read_csv(file)
data.drop_duplicates(inplace=True)

data['tag'] = '4'
data = data[['tag', 'mobileno']]

data.to_csv(r'龙江会员订购号码（全量）.txt', index=False)

# 匹配物联网卡号段
tmp = data.loc[data.mobileno.map(
    lambda x: ((len(str(x)) == 13 and (
            str(x)[:3] == '144' or str(x)[:5] == '10647' or str(x)[:5] == '10648')) or
              (len(str(x)) == 11 and (
            str(x)[:4] == '1476' or str(x)[:4] == '1724' or str(x)[:4] == '1789' or str(x)[:4] == '1849'))))]

tmp.to_csv(r'龙江会员订购号码（已匹配物联网号段）.txt', index=False)
