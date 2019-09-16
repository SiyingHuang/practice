# 根据所提供号码
# 匹配最新一天MaaP日活。
# 匹配Native存量：即，至今有过Native新增或活跃记录的号码。

import pandas as pd
import numpy as np

maap_data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_maap_0911.txt',
                        sep='|', header=None, usecols=[0], names=['mobileno'])
native_data = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_new_or_active_201908_and_before.txt',
    header=None, names=['mobileno'])

path = r'C:\Users\Administrator\Desktop\xqx0916-中信206万'
data = pd.read_csv(path+'.txt',
                     header=None, skiprows=1, names=['mobileno'])
tmp = pd.merge(data, maap_data, how='inner', on='mobileno')
tmp.to_csv(path+'（maap日活交集）.txt',
             header=None, index=False)

path = r'C:\Users\Administrator\Desktop\xqx0916-中信206万'
data = pd.read_csv(path+'.txt',
                     header=None, skiprows=1, names=['mobileno'])
tmp = pd.merge(data, native_data, how='inner', on='mobileno')
tmp.to_csv(path+'（Native历史用户（新增或活跃）交集.txt',
             header=None, index=False)