import pandas as pd
import numpy as np
import datetime

with open(r'C:\Users\Administrator\Desktop\native_cunliang_201908_no_active.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active\native_active_201906_and_before.txt',
                    sep='|', header=None)
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active\native_active_201907to201908.txt',
                    sep='|', header=None)
data2 = data2[data2[0].notnull()]
data2[0] = data2[0].astype(np.int64)
data = data1.append(data2)
data = data.drop_duplicates()

data = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\7-8月活\native_active_Aug.txt',
                   header=None, skiprows=0, names=['mobileno'])
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\7-8月活\native_active_July.txt',
                   header=None, skiprows=0, names=['mobileno'])
data = (data.append(data2)).drop_duplicates()
data['mobileno'] = data['mobileno'].astype('str')
data = data.loc[data['mobileno'].str.len() == 11]
data = data.loc[data['mobileno'].map(lambda x: str(x)[0] == '1')]
data['mobileno'] = data['mobileno'].astype(np.int64)
data.to_csv(r'C:\Users\Administrator\Desktop\育艺\7-8月活\native_active_07to08.txt',
            header=None, index=False)




data.to_csv(r'C:\Users\Administrator\Desktop\native_active_Aug.txt',
            sep='|', header=None, index=False)