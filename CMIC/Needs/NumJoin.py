"""
需求：找出交集号码的两种方式
    方法1：用merge方法
    方法2：用tuple求交集
"""


import numpy as np
import pandas as pd
import sys
import time

sys.getsizeof(data) / (1024 ** 2)  # 查看文件大小
data.info()  # 查看文件信息

# 不了解文件结构时，可先读取前i行文件
with open(r'C:\Users\Administrator\Desktop\育艺\Python匹配\1600W.txt', 'r', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
with open(r'C:\Users\Administrator\Desktop\育艺\139邮箱酷版日活明细_190801-03.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
with open(r'C:\Users\Administrator\Desktop\yuyi_yuyin_overorequal2_1to11.txt', 'r') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\139kuban_190801-03.txt',
                    sep='|', header=None, names=['mobileno', 'date'])
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\139kuban_190804-12.txt',
                    sep='|', header=None, names=['mobileno', 'date'])
data3 = pd.read_csv(r'C:\Users\Administrator\Desktop\yuyi_yuyin_overorequal2_1to11.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])

data1 = data1.loc[data1.prov != '上海']
data1 = data1.loc[data1.prov != '上海', ['mobileno']]
data2['target'] = 1
data2 = pd.concat((data1, data2), axis=0)

# 方法1：用merge方法
result = pd.merge(data2, data3, how='inner', on='mobileno')
# test
tmp1 = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                     'B': [1, 1, 1, 1, 1]})
tmp2 = pd.DataFrame({'A': [3, 4, 5, 6, 7]})
Result = pd.merge(tmp1, tmp2, how='inner', on='A')
Result = pd.merge(tmp1[['A']], tmp2, how='inner', on='A')

# 方法2：用tuple求交集
tmp3 = set(tmp1.A.values)
tmp4 = set(tmp2.A.values)
Result2 = tmp3 & tmp4
Result2 = pd.Series(list(Result2))

result['mobileno'].to_csv(r'C:\Users\Administrator\Desktop\yuyi_yuyin_jiaoyu0717to0808.txt',
                          header='False', index=False)
