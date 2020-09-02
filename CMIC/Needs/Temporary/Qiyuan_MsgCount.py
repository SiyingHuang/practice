"""
需求：
提取周期内Native消息日志
统计周期内消息总量
"""


import pandas as pd
import numpy as np

data_qy = pd.read_csv(r'C:\Users\Administrator\Desktop\qiyuan_msg.txt',
                      sep='|', header=None,
                      usecols=[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12],
                      names=['date', 'keep1', 'keep2', 'mobileno', 'keep3', 'brand', 'term', 'mess', 'txt', 'pic',
                             'vid', 'voi'])
data_qy['date'] = data_qy.loc[data_qy['date'].notnull()]['date'].astype(np.int32).astype('str')
tmp1 = data_qy.loc[(data_qy['date'].astype('str').between('20190812', '20190818')) | (data_qy['date'].isna())]
tmp1 = tmp1.iloc[:, 1:]
tmp2 = tmp1.groupby('mobileno')['mess', 'txt', 'pic', 'vid', 'voi'].sum()
tmp3 = pd.merge(tmp1.iloc[:, :6], tmp2, how='inner', on='mobileno')
tmp3.iloc[:, 6:11] = tmp3.iloc[:, 6:11].astype(np.int32)
tmp3.to_csv(r'C:\Users\Administrator\Desktop\qiyuan_msg_12to18.txt',
            header=None,
            index=False,
            sep='|')

tmp1 = data_qy.loc[(data_qy['date'].astype('str').between('20190819', '20190822')) | (data_qy['date'].isna())]
tmp1.to_csv(r'C:\Users\Administrator\Desktop\qiyuan_msg_19to22.txt',
            header=None,
            index=False,
            sep='|')
