import numpy as np
import pandas as pd
import os

path = r'C:\Users\Administrator\Desktop\native_main_users_half_year.txt'
path = r'C:\Users\Administrator\Desktop\native_called_users_half_year.txt'
data = pd.read_csv(path,
                   header=None, names=['mobileno',
                                       'p2p_mess_native', 'group_mess_native', 'group_counts_native',
                                       'p2p_mess_app', 'group_mess_app', 'group_counts_app',
                                       'p2p_mess_pc', 'group_mess_pc', 'group_counts_pc'],
                   dtype={'mobileno': np.int64})
ld = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\集团&专业公司-部门级别以上领导-20191101.txt',
                 header=None, usecols=[0, 1, 2, 3, 4], names=['name', 'mobileno', 'group', 'duty1', 'duty2'],
                 dtype={'mobileno': np.int64})
ld_1 = ld.loc[ld.mobileno != 13800000000]

result = pd.merge(ld_1, data, how='left', on='mobileno')
result.fillna(0, inplace=True)
result.iloc[:, 5:] = result.iloc[:, 5:].astype(np.int64)
result.to_csv(r'C:\Users\Administrator\Desktop\消息主叫情况.txt',
              header=None, index=False)


# 号码出现重复的清单
dul_num = ld.loc[ld['mobileno'].duplicated(), ['mobileno']].drop_duplicates()
pd.merge(ld, dul_num, how='inner', on='mobileno').sort_values(by='mobileno').to_excel(r'C:\Users\Administrator\Desktop\temp.xlsx',
                                                                        header=None, index=False)

