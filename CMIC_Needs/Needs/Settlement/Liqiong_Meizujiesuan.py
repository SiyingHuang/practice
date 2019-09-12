import pandas as pd
import numpy as np

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

data = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt',
    sep='|', header=None, usecols=[0, 1, 3], names=['date', 'mobileno', 'imei'], parse_dates=[0], dtype={'imei': 'str'})
tmp = data.sort_values(['date', 'imei'])
tmp = tmp.drop_duplicates(subset=['mobileno'], keep='first')
tmp2 = tmp.sort_values(['date', 'mobileno'])
tmp2 = tmp2.drop_duplicates(subset=['imei'], keep='first')
print(tmp2.shape[0])
tmp2.iloc[:, 1:].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\结算数据（号码+IMEI）.txt',
            sep='|', header=None, index=False)



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

# 与此前SQL提取结果出现差异
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