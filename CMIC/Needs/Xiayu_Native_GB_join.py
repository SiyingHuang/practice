# 分省提供号码包
# 需要匹配并输出3份号码包：
# 1、匹配指定周期内的Native活跃（非国标MaaP）用户；
# 2、匹配指定周期内的国标MaaP活跃用户；
# 3、剩余号码。

import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Administrator\Desktop\【叶旋】升档享购机券\升139元套餐享1200购机-11314161.txt',
                   header=None, names=['mobileno'])
data_if = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191204002_gd_native_if_GB.txt',
                      sep='|', header=None, names=['mobileno', 'if_gb'])
data_if['tag'] = 1
tmp = pd.merge(data, data_if, how='left', on='mobileno')
tmp.loc[tmp['tag'] == 1]
tmp.loc[((tmp['tag'] == 1) & (tmp['if_gb'] != 1)), ['mobileno']].to_csv(
    r'C:\Users\Administrator\Desktop\【叶旋】升档享购机券\升139元套餐享1200购机-11314161(native活跃不含国标maap).txt',
    header=None, index=False)
tmp.loc[((tmp['tag'] == 1) & (tmp['if_gb'] == 1)), ['mobileno']].to_csv(
    r'C:\Users\Administrator\Desktop\【叶旋】升档享购机券\升139元套餐享1200购机-11314161(国标maap).txt',
    header=None, index=False)
tmp.loc[tmp['tag'] != 1, ['mobileno']].to_csv(
    r'C:\Users\Administrator\Desktop\【叶旋】升档享购机券\升139元套餐享1200购机-11314161(剩余用户).txt',
    header=None, index=False)