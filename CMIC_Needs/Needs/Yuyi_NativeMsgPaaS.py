import pandas as pd
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
data_yy = pd.read_csv(r'C:\Users\Administrator\Desktop\yuyi_yuyin_overorequal2_1to11.txt',
                      sep='|', header=None, usecols=[0, 1],
                      names=['mobileno', 'yuyin'],
                      encoding='GBK')


# 【筛选符合消息量条件的号码】
data_yy_tmp = data_yy.loc[(data_yy['all'] >= 8) & (data_yy['all'] <= 23)]
data_yy_tmp = data_yy.loc[data_yy['all'] >= 24]
data_yy_tmp = data_yy.loc[data_yy['fmt'] >= 1]
data_yy_tmp = data_yy.loc[(data_yy['all'] >= 24) | (data_yy['fmt'] >= 1)]

data_yy_tmp[['mobileno']].to_csv(r'C:\Users\Administrator\Desktop\fmsg.txt',
                                 header=False, index=False)

# 【剔除异常号码】
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
data = pd.concat((data1, data2, data3, data4, data5, data6), axis=0)
data.reset_index(drop=True, inplace=True)  # inplace就地修改。或data = data.reset_index(drop=True)

data.info()
data['mobileno'] = data['mobileno'].astype('str')

data = data[data['mobileno'].str.len() == 11]
data = data[data['mobileno'].map(lambda x: str(x)[0] == '1')]

data.iloc[:,0].size

My_to_csv(data, '合并')


# 【浩宇下发消息需求】
data_yy = pd.read_csv(r'C:\Users\Administrator\Desktop\native_msg_07_middle.txt',
                      sep='|', header=None,
                      usecols=[0, 1, 2, 8],
                      names=['mobileno', 'term_brand', 'all', 'fmt'],
                      dtype={'term_brand': 'str'},
                      encoding='utf-8')
data_yy_tmp = data_yy.loc[data_yy['term_brand'] == '华为公版' ]
data_yy_tmp2 = data_yy.loc[data_yy['term_brand'] == '华为战略']
data_yy_tmp = data_yy_tmp.append(data_yy_tmp2)
data_yy_tmp = data_yy_tmp.loc[(data_yy['all'] >= 24) | (data_yy['fmt'] >= 1)]
data_yy_tmp.drop_duplicates()
data_yy_tmp[['mobileno']].to_csv(r'C:\Users\Administrator\Desktop\hy.txt',
                                 header=False, index=False)