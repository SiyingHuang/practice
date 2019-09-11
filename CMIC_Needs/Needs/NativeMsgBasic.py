import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_msg_statistics.txt',
                   sep='|', header=None, usecols=[0, 1, 13, 14, 15, 16, 17, 18, 19])
data.columns = ['date', 'mobileno', 'm25', 'm58', 'm812', 'm1214', 'm1417', 'm1719', 'm1922']
data['v'] = data['d'].map(lambda x: str(x)[:8])
data['v'].value_counts()
data['a'].value_counts()
tmp = data.loc[data['v'] == '20190714']
tmp['b'].drop_duplicates()