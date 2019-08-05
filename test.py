import pandas as pd

### pd.MultiIndex 构造多重索引

# 1、from arrays 从数组
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
# 2、from tuples 从元组
（1）
tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]
pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
# Out:
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])
（2）
tuples = [('cobra', 'mark i'), ('cobra', 'mark ii'),
          ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
          ('viper', 'mark ii'), ('viper', 'mark iii')]
index = pd.MultiIndex.from_tuples(tuples)
columns=['max_speed', 'shield']
values = [[12, 2], [0, 4],
          [10, 20], [1, 4],
          [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=columns, index=index)

### pd.DataFrame.stack()/unstack() 重塑
tmp = pd.DataFrame({'mobileno': list('aaabbb'),
                    'date': list('cdedef'),
                    'if_p_2_p': [1, 0, 1, 1, 1, 0]})
tmp2 = tmp.set_index(['mobileno', 'date']).unstack()


### pd.DataFrame
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
# （1）loc
df.loc['cobra'] #Series. But df.loc[['cobra']] --DataFrame
# （2）iloc
df.iloc[]