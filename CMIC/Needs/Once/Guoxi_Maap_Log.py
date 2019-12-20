# 处理南方BDOC中公众平台下发MaaP的日志
# 针对时间格式进行处理
# 并筛选出指定时间周期内的数据

import pandas as pd
import numpy as np
import datetime
import time

with open(r'C:\Users\Administrator\Desktop\hsy_tmp20190902002_maap0819to0820.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp20190902002_maap0819to0820.txt',
                   sep='|', header=None,
                   names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
sttime = data['c']
sttime.map(lambda x: datetime.datetime.strftime(datetime.datetime.strptime(str(x)[:10], '%Y-%m-%d'), '%Y-%m-%d'))  # 日期
sttime.map(
    lambda x: datetime.datetime.strftime(datetime.datetime.strptime(str(x)[11:19], '%H:%M:%S'), '%H:%M:%S'))  # 时间
sttime.map(lambda x: datetime.datetime.strptime(str(x)[:19], '%Y-%m-%dT%H:%M:%S'))  # 日期+时间
data['sttime'] = sttime.map(lambda x: datetime.datetime.strptime(str(x)[:19], '%Y-%m-%dT%H:%M:%S'))
data.loc[(data['sttime'] >= '2019-08-19 20:50:00') & (data['sttime'] <= '2019-08-19 22:00:00') | (
        data['sttime'] >= '2019-08-20 19:50:00') & (data['sttime'] <= '2019-08-20 21:00:00')]

datetime.datetime(2019, 1, 1, 12, 3, 40).date()