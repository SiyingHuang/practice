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

data = pd.read_csv(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_wqy_cscf_diffierent_time.txt',
                   sep='|', header=None, skiprows=0, usecols=[6, 7, 17], names=['mobileno', 'request', 'p_day_id'])

data.to_csv(r'C:\Users\Administrator\Desktop\native_active_Aug.txt',
            sep='|', header=None, index=False)
data = data[data['mobileno'].notnull()]
data['mobileno'] = data['mobileno'].astype(np.int64)

data.info()


# 入库时间与请求时间差异问题分析
data = pd.read_csv(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_wqy_cscf_diffierent_time.txt',
                   sep='|', header=None, skiprows=0, usecols=[6, 7, 17], names=['mobileno', 'request', 'p_day_id'])
data['request'] = data['request'].map(lambda x: str(x)[:8])
data['p_day_id'] = data['p_day_id'].map(lambda x: str(x)[:8])
data = data.drop_duplicates(subset='mobileno')
data1 = data[data['p_day_id'] == 20190803]
data1.mobileno.drop_duplicates()
data2 = data[data['p_day_id'] == 20190826]
data2.drop_duplicates()
data = data1.append(data2)
data.to_csv(r'C:\Users\Administrator\Desktop\cscf_different.txt',
            sep='|', header=None, index=False)

data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_cunliang_201908_no_active.txt',
                   header=None, names=['mobileno'])
data[data.duplicated()]