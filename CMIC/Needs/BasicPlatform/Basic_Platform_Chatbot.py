# Chatbot 下发效果统计
# 数据源：（1）消息中台日志（包括下行、上行触发下行）；
#         （2）基础平台（11201）日志统计。

import pandas as pd
import numpy as np
import os
import datetime

os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\01 - 【分析】\终端室需求\02.26 信息卡片与文案测试')
with open(r'消息中台\处理后\下行.txt', encoding='utf8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)


# 消息中台日志（下行、上行触发下行）
mp = pd.read_csv(r'消息中台\处理后\下行.txt', sep='|', header=None, dtype={2: 'str'},          # 下行日志
                 usecols=[0, 4], parse_dates=[0], names=['time', 'msg_id'])
mp = pd.read_csv(r'消息中台\处理后\下行ID.txt', sep='|', header=None,                          # 下行（仅消息ID字段）
                 names=['msg_id'])
mp = pd.read_csv(r'消息中台\处理后\触发的下行.txt', sep='|', header=None, dtype={2: 'str'},    # 触发的下行日志
                 usecols=[0, 4], parse_dates=[0], names=['time', 'msg_id'])
len('g302000003a70otffzbii1080k6a6oke5000')  # 消息ID长度：36
# 消息ID字段处理
mp['msg_id'] = mp['msg_id'].map(lambda x: str(x)[9:45])  # 消息中台下发的消息ID（消息ID长度：36）
# 区分 群聊or上行触发的下行（针对混合日志）
mp.loc[mp['msg_id'].map(lambda x: str(x)[:8]) == 'g3020000', 'type'] = '1'              # 群聊
mp.loc[mp['msg_id'].map(lambda x: str(x)[:8]) != 'g3020000', 'type'] = '2'              # 上行触发的下行
mp.info()  # time列格式为datetime64

# 基础平台下行日志
data_ori = pd.read_csv(r'基础平台下行日志.txt', sep='|', header=None, usecols=[1, 2, 15, 16, 17, 19, 20, 21, 24],
                       names=['main', 'called', 'status_code', 'r_time', 's_time', 'msg_id', 's_type', 'r_type',
                              'statis_hour'], dtype={16: 'str', 17: 'str'})
# 时间字段处理
data_ori['s_date'] = data_ori['s_time'].map(lambda x: str(x)[:14])  # 发送时间
data_ori['s_date'] = data_ori['s_date'].map(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d%H%M%S'))
data_ori['r_date'] = data_ori['r_time'].map(lambda x: str(x)[:14])  # 接收时间
data_ori['r_date'] = data_ori['r_date'].map(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d%H%M%S'))
# 被叫号码字段处理
data_ori['called'] = data_ori['called'].map(lambda x: str(x)[2:]).astype(np.int64)
# 区分 群聊or上行触发的下行（针对混合日志）
data_ori.loc[data_ori['msg_id'].map(lambda x: str(x)[:8]) == 'g3020000', 'type'] = '1'  # 群聊
data_ori.loc[data_ori['msg_id'].map(lambda x: str(x)[:8]) != 'g3020000', 'type'] = '2'  # 上行触发的下行
# 活动用户
users = pd.read_csv(r'推送号码.txt', sep='\t')


# （1）筛选时间范围
i = datetime.datetime(2020, 2, 26, 9, 54, 59)  # 起始时间
j = datetime.datetime(2020, 2, 28, 10, 20, 27)  # 结束时间
print(i, j)
data = data_ori.loc[(data_ori['s_date'] >= i) & (data_ori['s_date'] <= j)]  # 按发送时间统计
data = data_ori.loc[(data_ori['r_date'] >= i) & (data_ori['r_date'] <= j)]  # 按接收时间统计
data_ori.loc[(data_ori['s_date'] <= i) | (data_ori['s_date'] >= j)]
# （2）筛选指定消息ID
data = pd.merge(data, mp, how='inner', on='msg_id')  # 保留与消息中台ID相同的日志
# （3）匹配活动用户号码
data = pd.merge(data, users, how='inner', on='called')  # 匹配出活动号码

# 基础平台【发送时间】
data_s = data.loc[data['r_type'] == 7]  # 筛选出接收端为7的日志记录
data_s = data_s.sort_values(by=['called', 'msg_id', 's_time'], ascending=False)  # 按基础平台“called+msg_id+send_time”倒序排列
data_s_d = data_s.drop_duplicates(subset=['called', 'msg_id'], keep='first')  # 根据“号码+消息ID”去重，保留第一条记录
# 1、人数
data_s_d[['called', 'status_code', 'group']]
data_s_d[['called', 'status_code', 'group']].drop_duplicates(
    subset='called').groupby(
    by=['group', 'status_code']).count()['called']
# data_s_d.loc[(data_s_d['status_code'] == 2) & (data_s_d['r_type'] == 7), ['called', 'group']].drop_duplicates()['group'].value_counts()  # 法2
# 2、条数
data_s_d.loc[data_s_d['r_type'] == 7].groupby(by=['group', 'status_code']).count()['msg_id']
# data_s_d.loc[(data_s_d['status_code'] == 2) & (data_s_d['r_type'] == 7), 'group'].value_counts()

# 基础平台【接收时间】
data_r = data.loc[(data['status_code'].isin(['2', '3', '4'])) & (data['r_type'] == 7)]
# 1、人数
data_r.drop_duplicates(subset='called')['group'].value_counts().sort_index()
# 2、条数
data_r.drop_duplicates(subset='msg_id')['group'].value_counts().sort_index()
