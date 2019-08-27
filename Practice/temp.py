import pandas as pd
import numpy as np

with open(r'C:\Users\Administrator\Desktop\native_new_0819to0825.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\第三批匹配后\33to38.txt',
                   sep='|', header=None, usecols=[0], names=['mobileno'])
data['mobileno'] = data['mobileno'].map(lambda x: str(x)[:11])
data['mobileno'] = data['mobileno'].astype(np.int64)
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_0819to0825.txt',
                   sep='|', header=None, usecols=[0], names=['mobileno'])
data2['tag'] = 1
tmp = pd.merge(data, data2, how='left', on='mobileno')
tmp.loc[tmp['tag'] == 1]


gro = data_xiaomi.groupby('term')
gro.describe()