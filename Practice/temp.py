import pandas as pd
import numpy as np
import random
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs.txt',
                     header=None, usecols=[0], names=['mobileno'])
data = data.drop_duplicates()
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_0908.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])
# data2 = data2.drop_duplicates()
data2['tag'] = 1
Result = pd.merge(data, data2, how='left', on='mobileno')
Result = Result.loc[Result['tag'] == 1]
Result['mobileno'].to_csv(
    r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs（匹配后）.txt',
    header=None, index=False)





# 附件2
data_num_except2 = pd.read_csv(r'C:\Users\Administrator\Desktop\【请思颖协助】邮箱账单NPS调研号码筛选\附件2：9月和飞信账单群发的阅读用户清单_20190930需求1结果new.txt',
                              sep='|', header=None,
                              names=['mobileno'])
# Native用户8月消息明细
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\Native用户8月消息明细\Native用户8月消息明细.txt',
                              sep='|', header=None, usecols=[0], skiprows=1,
                              names=['mobileno'])
tmp = pd.merge(data_num_except2, data_num_except, how='inner', on='mobileno')

len(set(data_num_except2['mobileno'])-set(data_num_except['mobileno']))
tmp = pd.DataFrame(set(data_num_except2['mobileno'])-set(data_num_except['mobileno']), columns=['mobileno'])
data_num_except2.loc[data_num_except2.mobileno == 13578096628]
data_num_except.loc[data_num_except.mobileno == 13578096628]

13562366456,
13570260130,
13578096628,

# 执行剔除操作
Result = pd.merge(tmp, data_num_jituan,
                  how='left',
                  on='mobileno')
len(Result.loc[Result['tag'] == 2])
tmp2 = Result.loc[Result['tag'] == 2]
len(tmp2['mobileno'].drop_duplicates())
