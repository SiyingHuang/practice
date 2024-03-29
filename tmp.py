# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import os
import random
import datetime

with open(
        r'C:\Users\Administrator\Desktop\中间号\huadan_20191031.txt',
        encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

count = 0
f = open(r'C:\Users\Administrator\Desktop\中间号\huadan_20191031.txt',
         encoding='gbk')
for line in f.readlines():
    count = count + 1
print(count)



# 承宗提供的脚本
from preprocess.data_handler import DataHandler

data = pd.read_csv(r'C:\Users\Administrator\Desktop\chatbot_day_active_gd_mz_0512.txt',
                   header=None, names=['mobileno', 'city'], usecols=[0, 1])
dh = DataHandler(data=data)
dh.delete_blacklist()
dh.delete_staff()
result = dh.save()
result.to_csv(r'C:\Users\Administrator\Desktop\华为潜在用户-湖北（已剔除）.txt',
              header=None, index=False)


data_re = pd.read_csv(r'C:\Users\Administrator\Desktop\record2.txt\record2.txt',
                      header=None, skiprows=1, names=['mobileno'],
                      sep='@sep', engine='python',
                      encoding='utf-8')
import re
s = '15951153248	全国平-13961091659,袁小宽-15152951925,包昌金主任-649149,李庆东-18861093980,曹福荣-13914411988,王  强-15996064666,张宏晓-13921723882,谢  捷-13401224588,唐春兵-13815931593,张丙权-13914419777,吕爱民-13812481120,戴  嵩-13952635998,柳秧喜-13775674496,乔华平-13401222456,鲁安婕-13775799917,夏  骎-18805268001,卞剑飞-13815929969,陆寅坤-15261000399,孙敬东-13401224548,田文新-15961088559,全  泉-15961089236,郑  浩-15195212386,周  琴-13952673626,张  伟-15195231418'
pattern = re.compile(r'-(\d{11})')
pattern.findall(s)

ls = []
data_re['mobileno'].map(num_extract)

def num_extract(s):
    gp = re.findall(pattern, s)
    if gp:
        ls.append(gp)
    else:
        return None

ls2 = []
for i in ls:
    for j in i:
        ls2.append(j)

tmp = pd.DataFrame(pd.value_counts(ls2)).reset_index()
tmp.columns = ['mobileno', 'cnts']
tmp['sec'] = tmp['mobileno'].map(lambda x: str(x)[:7]).astype(np.int32)
tmp2 = pd.merge(tmp, data_section_prov,
                    how='inner',
                    on='sec')
tmp2.groupby(by='operator').sum()['cnts']
tmp2.to_csv(r'C:\Users\Administrator\Desktop\record2.txt\被叫号码本异网匹配结果.txt',
            index=False)


from collections.abc import Iterable


def unpack_list1(lss):
    if isinstance(lss, (list, tuple)):
        for i in lss:
            if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
                yield from unpack_list1(i)
            else:
                yield i
    else:
        yield lss

def unpack_list(lss):
    if isinstance(lss, Iterable) and not isinstance(lss, (str, bytes)):
        for i in lss:
            yield from unpack_list()
    else:
        yield lss


list(unpack_list1([1, [2, 3], 'string', b'01', [4, [5, 6]], (7, 8, (9, (10, (11, 12))))]))
list(unpack_list('apple'))
list(unpack_list1(1))


list1 = [0, 1, 2, 2, 3, 5, 6, 7, 8, 80, 11, 11]
list1.sort()
