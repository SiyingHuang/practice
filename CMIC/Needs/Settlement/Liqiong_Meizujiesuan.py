"""
需求：魅族结算
"""


import pandas as pd
import numpy as np

# 提取结算数据明细
# 字段：号码、型号
data = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt',
    sep='|', header=None, usecols=[0, 1, 3], names=['date', 'mobileno', 'imei'], parse_dates=[0], dtype={'imei': 'str'})
tmp = data.sort_values(['date', 'mobileno'])
tmp = tmp.drop_duplicates(subset=['imei'], keep='first')
tmp2 = tmp.sort_values(['date', 'imei'])
tmp2 = tmp2.drop_duplicates(subset=['mobileno'], keep='first')
print(tmp2.shape[0])
tmp2.iloc[:, 1:].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\结算数据（号码+IMEI）.txt',
                        sep='|', header=None, index=False)

# 提取结算数据明细
# 字段：DM日期、号码、型号、IMEI
with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt',
    sep='|', header=None, usecols=[0, 1, 2, 3], names=['date', 'mobileno', 'term_type', 'imei'], parse_dates=[0], dtype={'imei': 'str'})
tmp = data.sort_values(['date', 'mobileno', 'term_type'])
tmp = tmp.drop_duplicates(subset=['imei'], keep='first')
tmp2 = tmp.sort_values(['date', 'imei', 'term_type'])
tmp2 = tmp2.drop_duplicates(subset=['mobileno'], keep='first')
print(tmp2.shape[0])
tmp2.iloc[:, 1:].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\结算数据（DM日期+号码+型号+IMEI）.txt',
                        sep='|', header=None, index=False)