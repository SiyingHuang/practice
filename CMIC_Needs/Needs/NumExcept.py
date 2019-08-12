import pandas as pd
import numpy as np

data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\一众\华为_2-4_tichu.txt',
                      sep='|', header=None,
                      names=['mobileno'],
                      encoding='GBK')

data_num_mingan = pd.read_csv(r'C:\Users\Administrator\Desktop\敏感号码.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num_mingan['tag'] = 1

data_num_jituan = pd.read_csv(r'C:\Users\Administrator\Desktop\中国移动集团号码及组织树.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num_jituan = data_num_jituan['mobileno'].map(lambda x: str(x)[-11:-1])
data_num_jituan = pd.DataFrame(data_num_jituan)
data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('int')
data_num_jituan['tag'] = 2

Result = pd.merge(data_num_except, data_num_jituan,
                  how='left',
                  on='mobileno')
Result = Result.loc[Result['tag'] != 2]

def My_to_csv(data_ys, csv_name):
    data = data_ys[['mobileno']]
    name = csv_name
    data.to_csv(r'C:\Users\Administrator\Desktop\{}_tichu.txt'.format(name),
                header=False, index=False)

My_to_csv(Result, '其他')