import pandas as pd

with open(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\A组.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

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

data = data1.append([data2, data3, data4, data5, data6])

data[data['mobileno'].str.len() != '11']
My_to_csv(data, '合并')