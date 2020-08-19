import numpy as np
import pandas as pd
import os

obj = Series([-1, 0, 1, 2, 3]) # obj = Series(list((-1, 0, 1, 2, 3)))

X = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
X
X.index
X.values
X['a']
X[:'b']

population_dict = {'a': 123, 'b': 456}
population = pd.Series(population_dict)
population
population[:'b']

pd.Series(5, index=['a', 'b'])

states = pd.Series(['abcd', 'defg'], index=[1, 3])
states

data = pd.DataFrame({'pop': population, 'sta': states})
data['pop']
pd.DataFrame(population, columns=['population'])

pd.DataFrame(np.random.random((3,2)), columns=['a', 'b'], index=[0, 1, 2])

states[['a', 'd']]
states.loc[1:3]

data.pop is data['pop']
data['add'] = 'tag' + 'bcd'
data.T
data.loc[:'c', :'pop']
data.iloc[:2, :2]
data['rand'] = np.random.random(3)
data.loc[(data['pop'] > 0) & (data['rand'] != '0'), ['add', 'rand']]
data['cos'] = np.cos(data['rand'])

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4), index=['A', 'B', 'C', 'D'])
ser

df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                  columns=['A', 'B', 'C', 'D'])

np.exp(ser)
np.sin(df * np.pi / 4)

popu = pd.Series([2043, 3435, 10248], index=['japan', 'usa', 'china'], dtype=int)
area = pd.Series([242453214, 1254124312, 1251325423], index=['japan', 'aus', 'china'], dtype=int)
area / popu
area.add(popu, fill_value=0)
popu.index | area.index

A = pd.Series([2, 3, 4], index=[0, 1, 2])
B = pd.Series([4, 5, 6], index=[1, 2, 3])
A + B
A.add(B)
A.add(B, fill_value=0)
list('fdsgfwe')

C = pd.DataFrame(rng.randint(0, 20, (2, 4)),
                 columns=list('ABCD'))
C.stack().mean()

A = rng.randint(10, size=(3, 5))
A - A[0]

df = pd.DataFrame(A, columns=list('ABCDE'))
df - df.iloc[0]
df.subtract(df['B'], axis=0)

df.iloc[0, ::2]

X = np.array([1,  'a'])
X.sum()

X = pd.Series([1, np.NaN, None, 'hello'], index=list('abcd'))
[1, np.NaN, None]
X.isnull()
X.dropna()

X = pd.Series(np.arange(5), index=list('abcde'), dtype=int)
X[0] = np.nan
X[1] = None

X = pd.DataFrame([[1, None, 'hello'],
                  [2, np.nan, np.NaN]])
X.dropna()
X.dropna(axis=1, how='all')

X.fillna(method='bfill')


index = [('abby', 2010), ('abby', 2011),
         ('owen', 2010), ('owen', 2011)]
populations = [124312, 45614, 4654354, 43534]
pop = pd.Series(populations, index=index)
pop[:('owen', 2010)]
pop[[i for i in pop.index if i[0] == 'abby']]

index = pd.MultiIndex.from_tuples(index)
index
pop = pop.reindex(index)
pop['abby', 2011]
pop.unstack()
pop.unstack().stack()

pop_df = pd.DataFrame({'total': pop, 'other': [1, 2, 3, 4]})
pop_df.unstack()
pop_df2 = pop_df['other'] / pop_df['total']
pop_df2.unstack()

pop = pop.reindex(pd.MultiIndex.from_tuples(index))

data = {('abby', 2010): 1, ('abby', 2011): 2,
         ('owen', 2010): 3, ('owen', 2011): 4}
pop = pd.Series(data)
pop.index.names = ['name', 'year']

pop[2010]
pop[:, 2010]

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
data = np.round(np.random.rand(4, 6), 1)
data[:, ::2] *= 10
data += 37

health_data = pd.DataFrame(data, index=index, columns=columns)
health_data.iloc[:1, :2]
health_data.loc[(2013, 1), ('Bob', 'HR')]
idx = pd.IndexSlice
health_data.loc[idx[:2013, 2], idx[:, 'HR']]

pop_flat = pop.reset_index(name=('count'))
pop_flat.set_index(['name', 'year'])

data_mean = health_data.mean(level='year')
data_mean.mean(level='type', axis=1)

health_data.groupby(by=['year']).mean()

def make_df(cols, ind):
    """一个简单的DataFrame"""
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    # data = {c: [print(c, i) for i in ind] for c in cols}
    return pd.DataFrame(data, index=ind)

make_df('A', range(3))
make_df('ABC', range(2))

[0, 1] + [1, 3]
x = [0, 1]
y = [1, 3]
np.concatenate([x, y])
x + y

ser1 = pd.Series(list('ABC'), index=list('abc'))
ser2 = pd.Series(list('DEF'), index=list('abc'))
np.concatenate([ser1, ser2])
ser1.append(ser2)
pd.concat([ser1, ser2], ignore_index=True)
pd.concat([ser1, ser2])
np.concatenate([ser1, ser2])

x = make_df('AB', [0, 1])
y = make_df('BC', [2, 3])
y.index = x.index
print(pd.concat([x, y], axis=1))
tmp = pd.concat([x, y], keys=['a', 'b'])
tmp_flat = tmp.unstack()

pd.concat([x, y], join='inner')

"""
案例：美国各州的数据统计
"""
# 原始数据读取
os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\《Python数据科学手册》\PythonDataScienceHandbook-master\notebooks\data')
pop = pd.read_csv(r'state-population.csv')
areas = pd.read_csv(r'state-areas.csv')
abbrevs = pd.read_csv(r'state-abbrevs.csv')
# 合并 简称-人口 与 简称-全称 数据
merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', axis=1)  # 删除重复列
merged.isnull().any()  # 查看哪一列有缺失值
merged.loc[merged.population.isnull()]  # 查看缺失值情况
merged.loc[merged.state.isnull(), 'state/region'].unique()  # 查看全称缺失的国家有哪些
# 补充国家全称
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
# 合并面积数据
final = pd.merge(merged, areas, how='left', on='state')
final.isnull().any()
final['state'].loc[final['area (sq. mi)'].isnull()].unique()
final.loc[final['area (sq. mi)'].isnull()]
final.dropna(inplace=True)  # 剔除面积缺失的数据
# 取出2010年数据
data2010 = final.query("year == 2010 & ages == 'total'")
# data2010 = final.loc[(final.year == 2010) & (final.ages == 'total')]
data2010.head()
data2010.set_index('state', inplace=True)  # 设置'state'为索引列
density = data2010['population'] / data2010['area (sq. mi)']  # 计算人口密度
density.sort_values(ascending=False, inplace=True)  # 降序排列

"""
groupby()
"""
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df.max(axis='index')
df.max(axis='columns')
planets.dropna().describe()

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)})
df.groupby(by='key').min()['data']
df.groupby(by='key')['data'].min()

planets.groupby(by='method')['orbital_period'].median()
for (method, group) in planets.groupby(by='method'):
    print("{0:30s} shape={1}".format(method, group.shape))

planets.groupby(by='method')['year'].describe()

rng = np.random.RandomState(0)
df = pd.DataFrame({'key': list('ABCABC'),
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)})
# 累计
df.groupby(by='key').aggregate(['min', np.median, max])
df.groupby(by='key').aggregate({'data1': 'min',
                                'data2': 'max'})
# 过滤
def filter_func(x):
    return x['data2'].std() > 4
print(df)
print(df.groupby(by='key').std())
print(df.groupby(by='key').filter(filter_func))
# 转换
df.groupby(by='key').transform(lambda x: x - x.mean())
# 应用
def norm_by_data2(x):
    # x是一个分组数据的DataFrame
    x['data1'] /= x['data2'].sum()
    return x
print(df)
print(df.groupby(by='key').apply(norm_by_data2))

L = list('010120')
df.groupby(L).sum()

df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
df2.groupby(mapping).sum()
df2.groupby(str.lower).mean()
df2.groupby([str.lower, mapping]).sum()

'''
行星数据
'''
import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape