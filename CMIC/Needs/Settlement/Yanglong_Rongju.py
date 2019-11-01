# 海信结算数据处理
# 保证号码、IMEI均唯一

import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\融聚+海信\[融聚]MMDE20190603002_rj.txt',
                   sep='|', header=None, usecols=[0, 1, 2], names=['date', 'mobileno', 'imei'])

data.mobileno.drop_duplicates()
data.imei.drop_duplicates()

data.sort_values(by=['date', 'mobileno', 'imei'], ascending=True, inplace=True)
data.drop_duplicates(subset='imei', inplace=True)
data.drop_duplicates(subset='mobileno', inplace=True)