import pandas as pd
import numpy as np
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




with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt',
    sep='|', header=None, usecols=[0, 1, 3], names=['date', 'mobileno', 'imei'], parse_dates=[0])
data2 = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt',
    sep='|', header=None, usecols=[0, 1, 3], names=['date', 'mobileno', 'imei'], parse_dates=[0], dtype={'mobileno': np.int64, 'imei': 'str'})



tmp = data.sort_values('date')
tmp = tmp.drop_duplicates(subset=['imei'], keep='first')

tmp2 = data2.sort_values('date')
tmp2 = tmp2.drop_duplicates(subset=['imei'], keep='first')

t1 = data.loc[data.imei.map(lambda x: isinstance(x, int)), ['imei']]
t2 = data.loc[data.imei.map(lambda x: not isinstance(x, int)), ['imei']]
set(t1.imei.map(lambda x: str(x))) & set(t2.imei)

data.loc[data.imei == '867085035950388']
data.loc[data.imei == 867085035950388]
data.loc[(data.imei == '867085035950388') | (data.imei == 867085035950388)]  # 原因是read_csv是分块读取