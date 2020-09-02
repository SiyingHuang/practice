"""
需求：
商拓侧提供号码包
将其与指定周期内Native、MaaP等活跃用户进行匹配，并输出结果
如需进行剔除敏感号码操作，则通过NumExcept.py进行处理
"""


import pandas as pd
import numpy as np
import os

# 待匹配数据包
data = pd.read_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851-12.31国标MaaP用户匹配\王者-移动-3246851\王者-移动-3246851（剔重后）.txt',
                   header=None, names=['mobileno'])
no_data = pd.read_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851-12.31国标MaaP用户匹配\王者-移动-3246851\王者-移动-3246851（非交集用户）.txt',
                      header=None, names=['mobileno'])
data_num_except = pd.DataFrame(set(data['mobileno'])-set(no_data['mobileno']), columns=['mobileno'])



data = pd.read_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851\王者-移动-3246851.txt', sep='|', header=None,
                   names=['mobileno'])
data.drop_duplicates(inplace=True)  # 号码去重
data.to_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851\王者-移动-3246851（剔重后）.txt',
            header=None, index=False)
# 活跃明细数据
act = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_0105.txt',
                  header=None, names=['mobileno'])  # Native活跃明细
qb_act = pd.read_csv(r'C:\Users\Administrator\Desktop\20191230_I_DATA_CHATBOT_USER_DTL_D.txt',
                     sep='|', header=None, names=['mobileno'], usecols=[1], skiprows=1)  # 国标MaaP活跃明细
act['tag'] = 1
# 交集用户（data_num_except用于进一步剔除）
data_num_except = pd.DataFrame(set(data['mobileno']) & set(act['mobileno']), columns=['mobileno'])
Result.to_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851\王者-移动-3246851（交集且剔除后用户）.txt',
              header=None, index=False)
# 非交集用户
len(set(data['mobileno'])-set(act['mobileno']))
Result = pd.merge(data, act, how='left', on='mobileno')
Result.loc[Result['tag'] == 1]
Result.loc[Result['tag'] != 1, ['mobileno']].to_csv(
    r'C:\Users\Administrator\Desktop\王者-移动-3246851\王者-移动-3246851（非交集用户）.txt',
    header=None, index=False)
