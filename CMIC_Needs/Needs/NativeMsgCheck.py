import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_11201_log_0714.txt',
                   sep='|', header=None,
                   names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u'])
data['v'] = data['d'].map(lambda x: str(x)[:8])
data['v'].value_counts()
data['a'].value_counts()
tmp = data.loc[data['v'] == '20190714']
tmp['b'].drop_duplicates()