"""
用途：
1.根据VGOP日报表，对每一个日.xlsx文件中的本异网用户活跃数进行求和；
2.将每日求和后数据，汇总在同一个.xlsx文件中；
3.使用Excel中数据透视表，按月统计日均活跃数据。
"""


import numpy as np
import pandas as pd
import os
import time
from datetime import datetime


st = time.time()  # 开始计时

path = r'C:\Users\Administrator\Desktop\和飞信(2)\和飞信\Days'
file_list = os.listdir(r'C:\Users\Administrator\Desktop\和飞信(2)\和飞信\Days')
result = pd.DataFrame(columns=['省份', '活跃用户数', '和飞信企业成员'])
for file_name in file_list:
    if '和飞信' in file_name:
        file_name2 = file_name.replace('.xlsx', '')
        date = file_name2[-8:]  # 日期为文件名后8位

        data = pd.read_excel(os.path.join(path, file_name), engine='openpyxl',
                             skiprows=2, usecols=[0, 1, 2, 3, 4, 5, 6],
                             names=['省份',
                                    'mobi_active_cmcc', 'mobi_active_other',
                                    'active_cmcc', 'active_other',
                                    'etp_cmcc', 'etp_other'])

        data = data.loc[data['省份'] == '全国']

        data['手机客户端活跃用户数'] = data['mobi_active_cmcc'] + data['mobi_active_other']
        data['活跃用户数'] = data['active_cmcc'] + data['active_other']
        data['和飞信企业成员'] = data['etp_cmcc'] + data['etp_other']

        data = data.iloc[:, [0, 7, 8, 9]]
        date = datetime.strptime(date, '%Y%m%d')
        data['日期'] = datetime.strftime(date, '%Y/%m/%d')
        data['月份'] = date.month

        result = result.append(data)

result.reset_index(inplace=True)
result.drop(columns='index', inplace=True)
result = result[['月份', '日期', '省份', '手机客户端活跃用户数', '活跃用户数', '和飞信企业成员']]
result.to_excel(os.path.join(path, 'combine_result.xlsx'), index=False)

print('耗时{:.4f}秒'.format(time.time() - st))  # 计算耗时


'''
测试代码
'''
data = pd.read_excel(r'C:\Users\Administrator\Desktop\和飞信(2)\和飞信\Days\和飞信+业务报表_20200101.xlsx', engine='openpyxl',
                     skiprows=2, usecols=[0, 3, 4, 5, 6], names=['province', 'active_cmcc', 'active_other', 'etp_cmcc', 'etp_other'])
data = data.loc[data.province == '全国']
data['活跃用户数'] = data['active_cmcc'] + data['active_other']
data['和飞信企业成员'] = data['etp_cmcc'] + data['etp_other']
data = data.iloc[:, [0, 5, 6]]
data['date'] =

result.info()
tmp = result.copy()

date.astype(datetime)
result['日期'] = result['日期'].astype(datetime)

datetime.strftime(datetime.strptime(date, '%Y%m%d'), '%Y/%m/%d')