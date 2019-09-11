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