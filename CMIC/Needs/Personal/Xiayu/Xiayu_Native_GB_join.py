"""
需求：
分省提供号码包
需要匹配并输出3份号码包：
1、匹配指定周期内的Native活跃（非国标MaaP）用户；
2、匹配指定周期内的国标MaaP活跃用户；
3、剩余号码。
"""


import pandas as pd
import numpy as np
import os

os.chdir(r'C:\Users\Administrator\Desktop\1月广东10086标杆打造目标用户筛选')
data = pd.read_csv(r'APP20191-11-省统APP+H5累计_20191231剔除限定号码（含万能副卡）1121(剔除(1300)).txt',
                   header=None, names=['mobileno'], skiprows=1)
data_if = pd.read_csv(r'C:\Users\Administrator\Desktop\native_if_gb.txt',
                      sep='|', header=None, names=['mobileno', 'if_gb'])
data_if['if_native'] = 1
tmp = pd.merge(data, data_if, how='left', on='mobileno')
tmp.loc[tmp['if_native'] == 1]
data_num_except = tmp.loc[((tmp['if_native'] == 1) & (tmp['if_gb'] != 1)), ['mobileno']]
Result.to_csv(
    r'APP20191-11-省统APP+H5累计_20191231剔除限定号码（含万能副卡）1121(剔除(1300))(native活跃不含国标maap).txt',
    header=None, index=False)
data_num_except = tmp.loc[((tmp['if_native'] == 1) & (tmp['if_gb'] == 1)), ['mobileno']]
Result.to_csv(
    r'APP20191-11-省统APP+H5累计_20191231剔除限定号码（含万能副卡）1121(剔除(1300))(国标maap).txt',
    header=None, index=False)
tmp.loc[tmp['if_native'] != 1, ['mobileno']].to_csv(
    r'APP20191-11-省统APP+H5累计_20191231剔除限定号码（含万能副卡）1121(剔除(1300))(剩余用户).txt',
    header=None, index=False)
