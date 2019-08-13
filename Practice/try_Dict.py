import pandas as pd

# 匹配出月份的数字形式
tup1 = (1,)
tup2 = (2, 'th')
tup1 + tup2
print('th' in tup1)
tmp = pd.DataFrame({'year': [2019] * 6,
                    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']})
tmp_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6}
tmp['new_month'] = tmp['month'].map(tmp_dict)
