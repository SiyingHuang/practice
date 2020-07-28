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


index = [('abby', 2010), ('owen', 2011)]
populations = [124312, 45614]
pop = pd.Series(populations, index=index)
pop[:('abby', 2010)]