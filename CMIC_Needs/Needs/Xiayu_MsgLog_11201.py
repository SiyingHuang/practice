# RCS_11201消息日志提取
# 筛选指定日期、指定消息ID、指定号码等

import pandas as pd

with open(r'C:\Users\Administrator\Desktop\rcs_0815to0821.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

for i in range(26):
    print('\''+chr(i+ord('a'))+'\''+',', end='')
zimu = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(zimu)

data_msg = pd.read_csv(r'C:\Users\Administrator\Desktop\rcs_0816to0821.txt',
                       sep='|', header=None,
                       names=['a', 'b', 'c', 'd', 'e', 'f', 'g',
                              'h', 'i', 'j', 'k', 'l', 'm', 'n',
                              'o', 'p', 'q', 'r', 's', 't', 'u',
                              'v', 'w', 'x', 'y', 'z'])

# 取指定周期内日志
data_msg_tmp = data_msg.loc[data_msg['z'].between(20190816, 20190818)]
data_msg_tmp = data_msg_tmp.sort_values(by=['z'], ascending=True)
data_msg_tmp.to_csv(r'C:\Users\Administrator\Desktop\rcs_0816to0818.txt',
                    header=None, index=False, sep='|')
data_msg_tmp['t'].map(lambda x: str(x)[:6])

# 取指定号码的日志
filepath = r'C:\Users\Administrator\Desktop\native用户教育消息8月16日1743下发号码\16号下发的号码.xlsx'
data_num = pd.read_excel(filepath,
                         skiprows=1, header=None, usecols=[1], names=['mobileno'])
data_msg['num'] = data_msg['c'].map(lambda x: str(x)[-11:])
data_num['mobileno'] = data_num['mobileno'].astype('str')
pd.merge(data, data_2, how='inner', left_on='mobileno', right_on='num').to_csv(
    r'C:\Users\Administrator\Desktop\native用户教育消息8月16日1743下发号码\rcs_12520040123_0816to0820.txt',
    header=None, index=False, sep='|')