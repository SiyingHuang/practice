import pandas as pd
import numpy as np
import os

with open(r'C:\Users\Administrator\Desktop\yizhong_msg_sichuan_0801to0819.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_yy = pd.read_csv(r'C:\Users\Administrator\Desktop\native_msg_07_middle.txt',
                      sep='|', header=None,
                      names=['mobileno', 'term_brand', 'all', 'txt', 'pic', 'vid', 'voi', 'pla', 'fmt'],
                      dtype={'term_brand': 'str'},
                      encoding='utf-8')


# 【筛选符合消息量条件的号码】
# 1、消息量不为0的号码，再分层筛选
data_yy_tmp = data_yy.loc[(data_yy['all'] >= 8) & (data_yy['all'] <= 23)]
data_yy_tmp = data_yy.loc[data_yy['all'] >= 24]
data_yy_tmp = data_yy.loc[data_yy['fmt'] >= 1]
data_yy_tmp = data_yy.loc[data_yy['all'] >= 200, ['mobileno']]
# 2、消息量为0的用户（用周期内活跃用户，剔除1、中发消息量不为0的号码）
# 全量7月Native活跃号码
data_num_active = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\native_active_July.txt',
                      sep='|', header=None,
                      usecols=[0], names=['mobileno'])
data_num_active = data_num_active[data_num_active['mobileno'].map(lambda x: str(x)[0] == '1')].drop_duplicates()
data_num_active['mobileno'] = data_num_active['mobileno'].astype(np.int64)
# 需剔除有发过消息的号码
data_num = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\fmsg_not_zero.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num['tag'] = 1

data_yy_tmp = pd.merge(data_num_active, data_num, how='left', on='mobileno')
data_yy_tmp = data_yy_tmp.loc[data_yy_tmp['tag'] != 1]
data_yy_tmp['mobileno'].to_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\msg_total_zero(0826).txt',
              header=None, index=False)
# 输出结果
data_yy_tmp[['mobileno']].to_csv(r'C:\Users\Administrator\Desktop\fmsg.txt',
                                 header=False, index=False)


# 【合并多个txt文件】
txt_dict = {'msg_total_zero(0826)': 'A', 'msg_total_1to7': 'B', 'msg_total_8to23': 'C', 'msg_total_over24': 'D',
            'fmsg_over0': 'E', 'fmsg_over1': 'F'}
pieces = []
for txt_name, group in txt_dict.items():
    path = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\育艺\07.30 PaaS用户年龄分层匹配\%s.txt' % txt_name
    frame = pd.read_csv(path, names=['mobileno'])
    frame['group'] = group
    pieces.append(frame)
# 将所有数据合并到单个DataFrame中
data = pd.concat(pieces, ignore_index=True)

data['mobileno'] = data['mobileno'].astype('str') # 转为str，便于后续计算字段长度
data.reset_index


# 【剔除异常号码】
data = data[data['mobileno'].str.len() == 11]
data = data[data['mobileno'].map(lambda x: str(x)[0] == '1')]
data.iloc[:, 0].size
My_to_csv(data, '合并')


# 【将不同组别的号码输出到不同的txt文件中】
file_dict = {'1-重要价值': 'A', '2-一般价值': 'B', '3-一般发展': 'C', '4-重要挽留': 'D', '5-一般挽留': 'E', '6-新进入用户': 'F', '7-历史无需求': 'G', '8-流失用户': 'H'}
for file_name, group in file_dict.items():
    path = r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\用户分群结果&原始数据\筛选匹配结果\again\%s.txt' %file_name
    tmp = data_tmp.loc[data_tmp['group'] == group][['mobileno']]
    tmp.to_csv(path, header=None, index=False)