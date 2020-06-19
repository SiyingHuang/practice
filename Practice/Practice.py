import pandas as pd
import numpy as np
import time


# 【pd.MultiIndex 构造多重索引】
# 1、from arrays 从数组
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
# 2、from tuples 从元组
# （1）普通元组
tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]
pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
# Out:
MultiIndex(levels=[[1, 2], ['blue', 'red']],
           codes=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])
# （2）多重索引
tuples = [('cobra', 'mark i'), ('cobra', 'mark ii'),
          ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
          ('viper', 'mark ii'), ('viper', 'mark iii')]
index = pd.MultiIndex.from_tuples(tuples)
columns = ['max_speed', 'shield']
values = [[12, 2], [0, 4],
          [10, 20], [1, 4],
          [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=columns, index=index)


# 【pd.DataFrame.stack()/unstack() 重塑】
tmp = pd.DataFrame({'mobileno': list('aaabbb'),
                    'date': list('cdedef'),
                    'if_p_2_p': [1, 0, 1, 1, 1, 0]})
tmp2 = tmp.set_index(['mobileno', 'date']).unstack()


# 【pd.DataFrame】
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])
df.columns.size  # 列数
df.iloc[:, 0].size  # 行数，即获取“所有的行的第0列”的大小
# （1）loc 逗号前取行，逗号后取列
# 普通DataFrame
df.loc['cobra']  # Series. df.loc[['cobra']] --DataFrame
df.loc['cobra':'viper', ['shield']]  # --DataFrame
df.loc[df['max_speed'] == 4]
df.loc[df['max_speed'] == 4, ['shield']]  # --DataFrame
df[df['shield'] == 2]
df.loc[[True, False, True], ['shield']]  # --DataFrame
df1 = df.copy()
df1.loc[['cobra'], ['shield']] = 10
df1.loc['cobra'] = 10
df1.loc[:, 'shield'] = 2
# 多重DataFrame
df.loc[('cobra', 'mark i')]  # --Series
df.loc[('cobra', 'mark i'):'sidewinder']
df.loc[('cobra', 'mark i'):('sidewinder', 'mark i')]
# （2）iloc
df.iloc[0]
df.iloc[[0, 1]]
df.iloc[:2]
df.iloc[0, 1]
df.iloc[[0, 2], [1]]
df.iloc[1:2, 0:1]
df.iloc[:, [True, False]]


# 【to_csv函数】
# （1）自己写的太复杂的 to_csv 函数 →_→
def My_to_csv_own(data_ys):
    data = []
    for line in data_ys.index:
        data.append(data_ys.iloc[line])
    data = pd.DataFrame(data)[['mobileno']]
    data.to_csv(r'C:\Users\Administrator\Desktop\1.txt', header=False, index=False)

# （2）直接
def My_to_csv(data_ys, csv_name):
    data = data_ys
    name = csv_name
    data.to_csv(r'C:\Users\Administrator\Desktop\{}.txt'.format(name), header=False, index=False)
My_to_csv(data_yy_tmp, 'fmsg_over1')


# 【斐波那契数列】
# 1、普通函数法
def fab(num):
    t, a, b = 0, 0, 1
    while t < num:
        yield b  # yield出现，变成生成器函数
        # print(b)  # 普通函数法
        a, b = b, a + b  # 先完成等号右边的运算，再赋值给等号左边
        t = t + 1
fab_ = fab(9)  # fab_ 是生成器
list(fab_)
next(fab_)
# 尝试判断是否为生成器函数
from inspect import isgeneratorfunction
isgeneratorfunction(fab)        # fab 是生成器函数
isgeneratorfunction(fab(9))     # fab(9) 是生成器，而不是生成器函数
