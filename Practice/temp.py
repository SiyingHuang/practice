import pandas as pd
import numpy as np
import os
import random
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)





count = 0
f = open(r'C:\Users\Administrator\Desktop\hxmz_active_period_M_201909\hxmz_active_period_M_meizu_cunliang_201909.txt',
         encoding='utf-8')
for line in f.readlines():
    count = count+1
print(count)





data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\huawei_1to21.txt',
                    header=None, names=['mobileno'])
data1['mobileno'] = data1['mobileno'].map(lambda x: str(x)[:11])
data1['mobileno'] = data1['mobileno'].astype(np.int64)
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_1118to1124.txt',
                    header=None, names=['mobileno'])
len(pd.merge(data1, data2, how='inner', on='mobileno'))

data = pd.read_csv(r'C:\Users\Administrator\Desktop\270W小米native潜在用户\270W_xiaomi_miui10(验证).csv',
                   header=None, names=['mobileno', 'prov'], skiprows=1, usecols=[0, 1])
data.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\xiaomi_（各省份）_1201和飞信_120W.txt', sep='|', header=None, index=False)







data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_1214.txt',
                   sep='|', header=None, names=['mobileno', 'brand'])
data = data.loc[data['mobileno'].notna()]
data['mobileno'] = data['mobileno'].astype(np.int64)
data['brand'].value_counts()
data['tag'] = 1

data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\合并结果_2558847.txt',
                    header=None, names=['mobileno'])

Result = pd.merge(data2, data, how='left', on='mobileno')
Result.loc[Result['tag'] == 1]
Result.loc[Result['tag'] == 1, 'brand'].value_counts()
Result.loc[Result['tag'] == 1, ['mobileno', 'brand']].to_csv(r'C:\Users\Administrator\Desktop\合并结果_2558847（匹配后）.txt',
                                                             sep='|', header=None, index=False)
