import pandas as pd

path_home = r'E:\学习\充电\Python学习\流失用户分析\test1.csv'
path_comp = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\流失用户分析\test1.csv'
csv_path = path_home
csv_path = path_comp

data_ls = pd.DataFrame(pd.read_csv(csv_path, header=None, names=list(('mobileno','active_date','if_p_2_p')))[:10])
data_ls['if_active'] = 1
#交换列位置-法1
cols = list(data_ls)
cols.insert(2,cols.pop(cols.index('if_active')))
data_ls = data_ls.loc[:,cols]
#交换列位置-法2
data_ls = data_ls[list(('mobileno','active_date','if_active'))]

data_ls2 = data_ls.set_index(['mobileno','active_date'])
data_ls3 = data_ls2.unstack()

tmp = pd.DataFrame({'mobileno': list('aaabbb'),
                    'date': list('cdedef'),
                    'if_p_2_p': [1, 0, 1, 1, 1, 0]})
tmp2 = tmp.set_index(['mobileno', 'date'])
tmp3 = tmp2.unstack()