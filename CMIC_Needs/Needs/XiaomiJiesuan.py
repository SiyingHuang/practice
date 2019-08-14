import pandas as pd

with open(r'C:\Users\Administrator\Desktop\小米结算差异数据核查\jiesuan_new_active_notinour_jiesuan_check_20190814.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_jiesuan = pd.read_csv(
    r'C:\Users\Administrator\Desktop\小米结算差异数据核查\jiesuan_new_active_notinour_jiesuan_check_20190814.txt',
    sep='|', header=None, encoding='utf-8',
    names=['mobileno',
           'new', 'newb',
           'act12_1', 'act12_1b', 'act12_2', 'act12_2b',
           'act1b',
           'act2b',
           'act3b',
           'act4b',
           'act5b',
           'act6b',
           'act7b'])

tmp.columns

tmp = data_jiesuan.loc[data_jiesuan['new'].isna() & data_jiesuan['act12_1'].isna()].drop_duplicates('mobileno')
tmp.drop_duplicates('mobileno')