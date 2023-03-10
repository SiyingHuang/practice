# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/22
# @Author : Owen

"""
需求人：黄思颖
需求：合并系统部提供的梦网结算报表；查看系统部、生态部AP结算系统差异；匹配出差异的明细信息。
"""

import os
import pandas as pd

# 1、系统部梦网结算报表合并
path = r'D:\中移互联网\财务审计\【3】收集的资料\[系统部、生态部] 梦网报表\[系统部] 梦网结算报表'
os.chdir(path)

xls_list = []

for root, dirs, files in os.walk(path):
    # 遍历文件
    for f in files:
        if '账期D报表' in f and '全网梦网' in f:
            xls_list.append(os.path.join(root, f))
xls_list.remove('D:\\中移互联网\\财务审计\\【3】收集的资料\\[系统部、生态部] 梦网报表\\[系统部] 梦网结算报表\\201906_梦网结算报表\\201906_梦网结算报表\\中移互联网有限公司-全网梦网201906账期报表\\全网梦网201906账期D报表.xls')

data = []
for file in xls_list:
    tmp = pd.read_excel(file)
    data.append(tmp)

data = pd.concat(data, ignore_index=True)

data.to_excel(r'全网梦网账期D报表（201901-202102）.xlsx', index=False)


# 2、双方差异匹配
path = r'D:\中移互联网\财务审计\【3】收集的资料\[系统部、生态部] 梦网报表'
os.chdir(path)

data_xtb = pd.read_excel(r'201906-系统部-全网梦网账期D报表.xlsx', dtype={'计费月': 'str'})
data_stb = pd.read_excel(r'201906-生态部-AP结算系统-梦网业务原始报表.xls', dtype={'计费月': 'str'})

data_xtb = data_xtb.drop_duplicates()
data_stb = data_stb.drop_duplicates()

data_xtb = data_xtb[['计费月', 'SP名称', '上行条数', '下行条数']]
data_xtb['xtb'] = '1'

data_stb = data_stb[['计费月', 'SP名称', '上行条数', '下行条数']]
data_stb['stb'] = '1'

result1 = pd.merge(data_xtb[['计费月', 'SP名称', '上行条数', '下行条数']], data_stb, how='left',
                   on=['计费月', 'SP名称', '上行条数', '下行条数'])
result1.loc[result1.stb == '1']
result1.loc[result1.stb != '1'].count()
xt_yes_st_no = result1.loc[result1.stb != '1']

result2 = pd.merge(data_stb[['计费月', 'SP名称', '上行条数', '下行条数']], data_xtb, how='left',
                   on=['计费月', 'SP名称', '上行条数', '下行条数'])
result2.loc[result2.xtb == '1']


# 找出差异的40条记录对应的明细
data_xtb2 = pd.read_excel(r'[系统部] 全网梦网账期D报表（201901-202102）.xlsx', dtype={'计费月': 'str'})

data_xtb2 = data_xtb2.loc[data_xtb2['计费月'] == '201906']

result3 = pd.merge(xt_yes_st_no, data_xtb2, how='left', on=['计费月', 'SP名称', '上行条数', '下行条数'])
result3.to_excel(r'201906-系统部有而生态部没有的明细.xlsx', index=False)
