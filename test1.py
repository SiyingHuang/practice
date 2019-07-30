import pandas as pd

path_home = r'E:\学习\充电\Python学习\流失用户分析\test1.csv'
path_comp = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\流失用户分析\test1.csv'
csv_path = path_home
csv_path = path_comp

data_read = pd.DataFrame(pd.read_csv(path_comp)[:10])

tmp = pd.DataFrame({'mobileno': list('aaabbb'),
                    'active_date': list('cdedef'),
                    'if_p_2_p': [1, 0, 1, 1, 1, 0]})
tmp2 = tmp.set_index(['mobileno', 'date'])
tmp3 = tmp2.unstack()