import pandas as pd
import numpy as np

# 匹配出月份的数字形式
tup1 = (1,)
tup2 = (2, 'th')
tup1 + tup2
print('th' in tup1)
tmp = pd.DataFrame({'year': [2019] * 6,
                    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']})
tmp_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6}
tmp['new_month'] = tmp['month'].map(tmp_dict)

with open(r'C:\Users\Administrator\Desktop\qiyuan_basic_0812.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data = pd.read_csv(r'C:\Users\Administrator\Desktop\qiyuan_basic_0812.txt',
                   sep='|', header=None,
                   names=['mobileno', 'keep', 'prov', 'brand', 'term_type', 'first_new', 'days', 'if'],
                   encoding='utf-8')

data = data[['mobileno', 'keep', 'first_new', 'prov', 'brand', 'term_type', 'days', 'if']]
data.to_csv(r'C:\Users\Administrator\Desktop\qiyuan_basic_0812_2.txt',
            sep='|', header=None, index=False)