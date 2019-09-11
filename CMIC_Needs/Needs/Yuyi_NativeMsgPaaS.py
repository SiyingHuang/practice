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
data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\msg_total_zero.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data1['group'] = 'A'

data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\msg_total_1to7.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data2['group'] = 'B'

data3 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\msg_total_8to23.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data3['group'] = 'C'

data4 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\msg_total_over24.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data4['group'] = 'D'

data5 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\fmsg_over0.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data5['group'] = 'E'

data6 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\07.30 PaaS用户年龄分层匹配\fmsg_over1.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data6['group'] = 'F'


data = data1.append([data2, data3, data4, data5, data6])  # 只能append至末尾。
data = pd.concat((data1, data2, data3, data4, data5, data6), axis=0)  # 或用concat拼接，axis=0表示按行拼接。
data.reset_index(drop=True, inplace=True)  # inplace就地修改。或data = data.reset_index(drop=True)

data.info()
data['mobileno'] = data['mobileno'].astype('str') # 转为str，便于后续计算字段长度
data.reset_index


# 【剔除异常号码】
data = data[data['mobileno'].str.len() == 11]
data = data[data['mobileno'].map(lambda x: str(x)[0] == '1')]
data.iloc[:, 0].size
My_to_csv(data, '合并')