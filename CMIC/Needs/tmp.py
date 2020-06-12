# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import os
import random
import datetime

with open(
        r'C:\Users\Administrator\Desktop\黑名单.txt',
        encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

count = 0
f = open(r'C:\Users\Administrator\Desktop\20191230_I_DATA_CHATBOT_USER_DTL_D.txt',
         encoding='utf-8')
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



bl = []
for i in black_list:
    bl.append(i)

result = pd.concat(bl, ignore_index=True)

# result.loc[(result.mobileno.map(lambda x: len(str(x)) != 11)) | (~result.mobileno.map(lambda x: str(x).startswith('1')))]
result = result.loc[(result.mobileno.map(lambda x: len(str(x)) == 11)) & (result.mobileno.map(lambda x: str(x).startswith('1')))]

result.to_csv(r'黑名单处理后.txt', index=False)
data2 = pd.read_csv(r'黑名单处理后.txt', header='infer')

data = data1.append(data2)
data.drop_duplicates(inplace=True)
data.to_csv(r'黑名单处理后.txt', index=False)



os.chdir(r'C:\Users\Administrator\Desktop')
data = pd.read_csv(r'native_mz_3months_active_3months_dm.txt', dtype={0: 'str', 3: 'str'}, header=None,
                   names=['mobileno', 'a', 'b', 'c'])
ld = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\集团内部员工名单\qy0402.csv',
                   dtype={'mobileno': 'str'}, header=None, names=['a', 'b', 'mobileno', 'c', 'd', 'e'])
ld = ld.loc[(ld['c'].map(lambda x: '领导' in str(x))) | (ld['d'].map(lambda x: '总经理' in str(x))) | (
    ld['d'].map(lambda x: '副总经理' in str(x)))]
ld.loc[ld.mobileno.map(lambda x: len(str(x)) != 11)]
result1 = pd.merge(data, ld, how='inner', on='mobileno')
result1.to_csv(r'leader_user.txt',
               header=None, index=False)
