import pandas as pd
import sys
import time

with open(r'C:\Users\Administrator\Desktop\育艺\匹配\139邮箱酷版日活_190722-31.txt', 'r') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\匹配\139邮箱酷版日活_190722-31.txt',
                   sep='|', header=None, names=['mobileno', 'date'])
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\育艺\匹配\139邮箱酷版日活_190722-31.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])

sys.getsizeof(data)/1024**2
data.info()

data = data.loc[data.date != 22].copy()
data = data.loc[data.date != 22,['mobileno']]
data2['target'] = 1
result = pd.merge(data, data2, how='inner', on='mobileno')


# test
tmp1= pd.DataFrame({'A':[1,2,3,4,5],
                     'B':[1,1,1,1,1]})
tmp2= pd.DataFrame({'A':[3,4,5,6,7]})
Result = pd.merge(tmp1, tmp2, how='inner', on='A')
Result = pd.merge(tmp1[['A']], tmp2, how='inner', on='A')

tmp3 = set(tmp1.A.values)
tmp4 = set(tmp2.A.values)
Result = tmp3 & tmp4
Result = pd.Series(list(Result))