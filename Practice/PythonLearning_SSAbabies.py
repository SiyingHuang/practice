import pandas as pd

names1880 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\babynames\yob1980.txt',
                        sep=',', header=None, names=['name', 'sex', 'births'])

# 组装所有txt文件
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\babynames\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, axis=0, ignore_index=True)  # 不保留读取每个csv文件时返回的原始行号

# 查看各年份男女婴的出生数
total_births = names.pivot_table(index='year', columns='sex', values='births',
                                 aggfunc='sum')  # total_births.plot(title='Total births by sex and year') 绘制图像

# 统计指定名字的出生数在某年某性别中所占的比例
def add_prop(group):
    births = group.births  # 如果为Python3以下版本，则需要执行此语句，先将births字段转为float格式后计算
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(
    add_prop)  # 按year（年份）和sex（性别）分组后统计。即，统计某个名字的出生数在某年某性别中所占的比例（分子为该名字的出生数，分母为names.groupby(['year', 'sex']).sum()）。
np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)  # 检查每个分组的prop值的总和是否等于或近似为1

# 取出每个year/sex对的出生数前1000个名字
def get_top100(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top100 = grouped.apply(get_top100)  # 对每个year/sex对，取出生数前1000的名字
