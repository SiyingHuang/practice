import pandas as pd

with open(r'C:\Users\Administrator\Desktop\native_msg_0726to0801_middle.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_yz = pd.read_csv(r'C:\Users\Administrator\Desktop\native_msg_0726to0801_middle.txt',
                      sep='|', header=None,
                      names=['mobileno', 'group', 'all', 'txt', 'pic', 'vid', 'voi', 'pla', 'fmt'],
                      encoding='GBK')

data_yz_tmp = data_yz.loc[data_yz['all'].notna()
                          & data_yz['all'] != 0]  # all是Python方法，不能直接data_yz.all
data_yz_tmp2 = data_yz_tmp.loc[data_yz_tmp['voi'] != 0]
data_yz_tmp3 = data_yz_tmp.loc[data_yz_tmp.fmt.notna() & data_yz_tmp.fmt != 0]

My_to_csv(data_yz_tmp)

data_yz_tmp3[['mobileno', 'group']].to_csv(r'C:\Users\Administrator\Desktop\fmt_not_zero.txt',
                                  header=False, index=False)