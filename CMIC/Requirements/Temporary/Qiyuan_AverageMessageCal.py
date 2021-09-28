"""
需求：剔除指定端口号
撰写人：詹承宗
"""


import pandas as pd
import os
from datetime import datetime

os.chdir(r'C:\Users\Administrator\Desktop\小王子需求')

data = pd.read_csv('运营原始号码.csv')
data.drop_duplicates(subset=['mobileno', 'group'], inplace=True)
tmp = pd.read_csv('qy_num_messcnt.txt', header=None, names=['mobileno', 'mess_cnt', 'date'], parse_dates=[2])
data = pd.merge(data, tmp, how='left', on='mobileno')


# 创建“日期-日期范围”字典
hy_gp = {}  # 浩宇
yy_gp = {}  # 育艺
yx_gp = {}  # 雁询

for dt in pd.date_range('2019-12-16', '2020-01-20'):
    if dt <= datetime(2019, 12, 22):
        hy_gp[dt] = '1216-1222'
    elif dt <= datetime(2019, 12, 23):
        hy_gp[dt] = '1223'
    elif dt <= datetime(2019, 12, 31):
        hy_gp[dt] = '1224-1231'
    elif dt <= datetime(2020, 1, 3):
        hy_gp[dt] = '0101-0103'
    else:
        hy_gp[dt] = '0104-0120'

for dt in pd.date_range('2019-12-22', '2020-01-20'):
    if dt <= datetime(2019, 12, 28):
        yy_gp[dt] = '1222-1228'
    elif dt <= datetime(2019, 12, 29):
        yy_gp[dt] = '1229'
    elif dt <= datetime(2020, 1, 1):
        yy_gp[dt] = '1230-0101'
    else:
        yy_gp[dt] = '0102-0120'

for dt in pd.date_range('2019-12-24', '2020-01-20'):
    if dt <= datetime(2019, 12, 30):
        yx_gp[dt] = '1224-1230'
    elif dt <= datetime(2019, 12, 31):
        yx_gp[dt] = '1231'
    elif dt <= datetime(2020, 1, 3):
        yx_gp[dt] = '0101-0103'
    else:
        yx_gp[dt] = '0104-0120'


data.head()
# 根据不同分组，匹配出对应日期范围
data.loc[data.group == 'hy', 'hy_gp'] = data.loc[data.group == 'hy', 'date'].map(hy_gp)
data.loc[data.group == 'yy', 'yy_gp'] = data.loc[data.group == 'yy', 'date'].map(yy_gp)
data.loc[data.group == 'yx', 'yx_gp'] = data.loc[data.group == 'yx', 'date'].map(yx_gp)

for col in ['hy_gp', 'yy_gp', 'yx_gp']:
    data[col] = data[col].astype('category')  # 将日期范围，改为category(类别)格式

data['hy_gp'].cat.reorder_categories(['1216-1222', '1223', '1224-1231', '0101-0103', '0104-0120'], inplace=True)
hy_gp_days = {'1216-1222': 7,
              '1223': 1,
              '1224-1231': 8,
              '0101-0103': 3,
              '0104-0120': 16}

data['yy_gp'].cat.reorder_categories(['1222-1228', '1229', '1230-0101', '0102-0120'], inplace=True)
yy_gp_days = {'1222-1228': 7,
              '1229': 1,
              '1230-0101': 3,
              '0102-0120': 18}

data['yx_gp'].cat.reorder_categories(['1224-1230', '1231', '0101-0103', '0104-0120'], inplace=True)
yx_gp_days = {'1224-1230': 7,
              '1231': 1,
              '0101-0103': 3,
              '0104-0120': 16}


# 对各分组，计算日均消息条数
"""浩宇分组"""
result = data.loc[data.group == 'hy'].groupby(['mobileno', 'hy_gp'])['mess_cnt'].sum().unstack()  # 计算号码在不同日期范围内的消息总条数
result.fillna(0, inplace=True)
for col in result.columns:                          # unstack()后，result.columns变成'hy_gp'列中的值（即不同的日期范围）
    result[col] = result[col] / hy_gp_days[col]     # 计算日均消息条数
tmp1 = result.copy()

"""育艺分组"""
result = data.loc[data.group == 'yy'].groupby(['mobileno', 'yy_gp'])['mess_cnt'].sum().unstack()
result.fillna(0, inplace=True)
for col in result.columns:
    result[col] = result[col] / yy_gp_days[col]
tmp2 = result.copy()

"""雁询分组"""
result = data.loc[data.group == 'yx'].groupby(['mobileno', 'yx_gp'])['mess_cnt'].sum().unstack()
result.fillna(0, inplace=True)
for col in result.columns:
    result[col] = result[col] / yx_gp_days[col]
tmp3 = result.copy()

writer = pd.ExcelWriter('3项活动分时段消息均值.xlsx')  # 存入同一个.xlsx文件中
tmp1.to_excel(writer, sheet_name='浩宇')
tmp2.to_excel(writer, sheet_name='育艺')
tmp3.to_excel(writer, sheet_name='雁询')
writer.save()
