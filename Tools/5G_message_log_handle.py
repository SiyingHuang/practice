# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
需求人：唐玲淑
用途：年报数据核查
    1.对5G消息 8+互联网 大区原始注册日志进行解析；
    2.筛选符合条件的日志；
    3.提取出品牌、机型、号码、省份等信息。
"""

import pandas as pd
import re
import time
import os
os.chdir(r'D:\Data\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】\UP_ALL_20210220')


"""正则匹配测试"""
log = pd.read_csv(r'F:\HN20201113\UP0820201113010001.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python')
data1 = log.loc[(log['ua'].map(lambda x: 'UP_2.4' in x)) & (log['ua'].map(lambda x: 'Meiz' not in x))]

# 数据样例
s = 'CPM-client/OMA2.2 RCS-client/UP_2.4 term-Mi/MI_Mi-10-V12.0.8.0.QJBCNXM client-JUPH/GB-2.0 OS-Android/V12.0.8.0.QJBCNXM;urn%3Aurn-7%3A3gpp-application.ims.iari.rcs.chatbot.sa;"+g.gsma.rcs.botversion=""#=1,#=2""";sip:+8613556425541@gd.5GMC.ims.mnc000.mcc460.3gppnetwork.org'
s = 'UP_2.4 term-Samsung/SM-G9860-G9860ZCU2BTH6 client_Samsung/IMS 6.0 OS-Android/sip:+8618303118287he.5GMC.ims.mnc000.mcc460.3gppnetwork.org'

# 正则匹配规则
pattern = re.compile(r'UP_2.4 term-(.*)/(.*) client.*sip:\+86(\d*)@(.*?)\.')    # 提取：品牌、机型、号码、省份代码
pattern = re.compile(r'.*sip:\+86(\d*).*')                                      # 仅提取号码
gp = re.search(pattern, s)
gp.group(1)
gp.groups()


# 1、分块读取处理：筛选出符合条件日志
st = time.time()  # 计时开始

log_up = pd.read_csv(r'UP.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python', chunksize=100000)  # 分块读取原始日志
# chatbot_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】\UP24list\UP24list.txt', header=None,
#                            sep='sep@@', names=['ua'],
#                            engine='python')
chatbot_data = []

"""筛选出UP2.4终端日志"""
for i in log_up:
    # UP2.4口径
    tmp = i.loc[(i['ua'].map(lambda x: 'UP_2.4' in x)) & (  # 含 “UP_2.4”
        i['ua'].map(lambda x: 'Meiz' not in x)) & (         # 不含 “Meiz”
        i['ua'].map(lambda x: 'GB' not in x))]              # 不含 “GB”
    chatbot_data.append(tmp)

chatbot_data = pd.concat(chatbot_data, ignore_index=True)   # 不保留原始索引
del tmp

print('耗时{:.4f}秒'.format(time.time() - st))  # 计算耗时

chatbot_data.to_csv(r'符合3个条件原始日志.txt',  # 原始日志输出
                    header=None, index=False)


"""关键信息提取函数"""
def extract_brand(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(1)
    else:
        return 'else'


def extract_term(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(2)
    else:
        return 'else'


def extract_mobileno(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(3)
    else:
        return 'else'
# """仅提取号码时"""
# def extract_mobileno(s):
#     gp = re.search(pattern, s)
#     if gp:
#         return gp.group(1)
#     else:
#         return 'else'


def extract_prov(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(4)
    else:
        return 'else'


# 2、提取所需信息：品牌、机型、号码、省份
st = time.time()  # 计时开始

result = pd.DataFrame(columns=['brand', 'term', 'mobileno', 'code'])
# result = pd.DataFrame(columns=['mobileno'])
result['brand'] = chatbot_data['ua'].map(extract_brand)       # 品牌
result['term'] = chatbot_data['ua'].map(extract_term)         # 机型
result['mobileno'] = chatbot_data['ua'].map(extract_mobileno)   # 号码
result['code'] = chatbot_data['ua'].map(extract_prov)         # 省份编码

print('耗时{:.4f}秒'.format(time.time() - st))  # 计算耗时


"""数据去重"""
# 包含四个字段
result = result.drop_duplicates()  # 全量去重
result.to_csv(r'符合3个条件处理后4个字段（去重）.txt',
              index=False)
# result = pd.read_csv(r'符合3个条件处理后4个字段.txt', dtype='str')
# 仅号码
result = result[['mobileno']].drop_duplicates()
result.to_csv(r'符合3个条件处理后仅号码字段（去重）.txt',
              index=False)

"""汇总统计"""
tmp = result.groupby(by=['code', 'brand', 'term'])['mobileno'].count()  # 去重后统计
tmp = tmp.reset_index(drop=False)


# 3、分省匹配
prov_code = pd.read_excel(r'D:\Data\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】\5G消息各大区省份编码.xlsx',
                          names=['code', 'prov'])  # “编码-省份”映射表
tmp2 = pd.merge(tmp, prov_code, on='code')  # code字段匹配省份信息
tmp2.to_excel(r'汇总统计.xlsx', index=False)
