# 根据所提供号码
# 1、匹配最新一天MaaP日活。
# 2、匹配Native存量：即，至今有过Native新增或活跃记录的号码。

import pandas as pd
import numpy as np

maap_data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_maap_0918.txt',
                        sep='|', header=None, usecols=[0], names=['mobileno'])
native_data = pd.read_csv(r'C:\Users\Administrator\Desktop\\native_active_0921.txt',
                          header=None, names=['mobileno'])

path = r'C:\Users\Administrator\Desktop\烦请鱼智科技12.4W匹配9月17日Native每日活跃数据'
data = pd.read_csv(path+'.txt',
                     header=None, skiprows=1, names=['mobileno'])
tmp = pd.merge(data, maap_data, how='inner', on='mobileno')
tmp.to_csv(path+'（MaaP日活交集）.txt',
             header=None, index=False)
tmp = pd.merge(data, native_data, how='inner', on='mobileno')
tmp.to_csv(path + '（Native日活交集）.txt',
           header=None, index=False)
