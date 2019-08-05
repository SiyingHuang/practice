import pandas as pd

path_home = r'E:\学习\充电\Python学习\流失用户分析\test1.csv'
csv_path = path_home

path_comp = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\流失用户分析\test1.csv'
csv_path = path_comp

data = pd.DataFrame(pd.read_csv(csv_path, header=None, names=list(('mobileno', 'active_date', 'if_p_2_p')))[:10])
data['if_active'] = 1

# 交换列位置-法1
cols = list(data)
cols.insert(2, cols.pop(cols.index('if_active')))
data = data.loc[:, cols]
# 交换列位置-法2
data = data[list(('mobileno', 'active_date', 'if_active'))]

data_ls = data[list(('mobileno', 'active_date', 'if_active'))]
data_ls2 = data_ls.set_index(['mobileno', 'active_date']).unstack()
data_ls2.columns = data_ls2.columns.levels[1]

data_ls2.index
data_ls2.columns

data_ls2.iloc[0]
data_ls2.loc[13903523283]

data_msg = data[list(('mobileno', 'active_date', 'if_p_2_p'))]
