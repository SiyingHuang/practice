import pandas as pd
import numpy as np

with open(r'C:\Users\Administrator\Desktop\anhui_cscf_returncode.txt',
          encoding='utf-8') as f:
    for i in range(5):
        temp = f.readline()
        print(temp)

data_cscf = pd.read_csv(r'C:\Users\Administrator\Desktop\anhui_cscf_returncode.txt',
                        sep='|', header=None)
data_cscf = data_cscf.loc[(data_cscf[4] != -1) & (data_cscf[4] != -3) & (data_cscf[4] != 401)]
data_cscf = data_cscf.drop_duplicates()
data_cscf = data_cscf.sort_values(by=0) # 按日期一列升序排列

data_cscf.to_csv(r'C:\Users\Administrator\Desktop\anhui_cscf_returncode_not_success.txt',
                 sep='|', header=None, index=False)

# 找出重复数据有哪些
data1 = data_cscf.drop_duplicates(keep=False)  # 删去所有重复数据
data2 = data_cscf.drop_duplicates(keep='first')  # 重复数据仅保留首条
data_duplicates = data2.append(data1).drop_duplicates(keep=False)  # 找出重复数据
# 挑出个别重复的数据查看
data_cscf.loc[(data_cscf[0] == 20190727) & (data_cscf[1] == 15805696633)].drop_duplicates()
data_cscf.loc[(data_cscf[0] == 20190727)].drop_duplicates()