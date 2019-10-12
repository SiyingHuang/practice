import pandas as pd

names1880 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\babynames\yob1980.txt',
                        header=None, names=['name', 'sex', 'births'])

# 组装所有txt文件
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\babynames\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)

# 查看各年份男女婴的出生数
total_births = names.pivot_table(index='year', columns='sex', values='births',
                                 aggfunc='sum')  # total_births.plot(title='Total births by sex and year')

# 统计指定名字的出生数所占的比例
def add_prop(group):
    births = group.births  # 如果为Python3以下版本，需要先将births字段转为float格式后计算
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)  # 按year（年份）和sex（性别）分组后统计


names.groupby(['year', 'sex']).sum()

