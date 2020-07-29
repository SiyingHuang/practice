import numpy as np
import pandas as pd

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
