import pandas as pd

with open(r'C:\Users\Administrator\Desktop\native_msg_07_middle.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_yy = pd.read_csv(r'C:\Users\Administrator\Desktop\native_msg_07_middle.txt',
                      sep='|', header=None,
                      names=['mobileno', 'all', 'txt', 'pic', 'vid', 'voi', 'pla', 'fmt'],
                      encoding='GBK')

data_yy_tmp = data_yy.loc[(data_yy['all'] >= 8) & (data_yy['all'] <= 23)]
data_yy_tmp = data_yy.loc[data_yy['all'] >= 24]
data_yy_tmp = data_yy.loc[data_yy['fmt'] >= 1]

data_yy_tmp[['mobileno']].to_csv(r'C:\Users\Administrator\Desktop\fmsg_over0.txt',
                                 header=False, index=False)

# Own
def My_to_csv2(data_ys):
    data = []
    for line in data_ys.index:
        data.append(data_ys.iloc[line])
    data = pd.DataFrame(data)[['mobileno']]
    data.to_csv(r'C:\Users\Administrator\Desktop\1.txt', header=False, index=False)

# 直接
def My_to_csv(data_ys, csv_name):
    data = data_ys.copy()
    data.to_csv(r'C:\Users\Administrator\Desktop\1.txt', header=False, index=False)

My_to_csv(data_yy_tmp)



