# 指定周期内
# Native拉新转化率、Native N=1转化率

import pandas as pd
import numpy as np
import os

os.chdir(r'C:\Users\Administrator\Desktop')
# 待匹配数据
data_ori = pd.read_csv(r'C:\Users\Administrator\Desktop\Native1月拉新（匹配后）\combine.txt',
                       header=None, names=['mobileno'])
data_ori = pd.read_csv(r'【湖北号码需求提醒】12月2日需求\huawei9_湖北.txt',
                       header=None, names=['mobileno'])
# 新增用户
data_new = pd.read_csv(r'native_new_0114to0120.txt',
                       header=None, names=['mobileno'])
# N=1用户
data_msg = pd.read_csv(r'native_msg_count_1219to1222.txt',
                       header=None, names=['mobileno'])
# 匹配操作
len(pd.merge(data_ori, data_new, how='inner', on='mobileno'))
len(pd.merge(data_ori, data_msg, how='inner', on='mobileno'))
