import pandas as pd
import numpy as np
import os

os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析')
names1880 = pd.read_csv(r'pydata-book-2nd-edition\datasets\babynames\yob1980.txt',
                        sep=',', header=None, names=['name', 'sex', 'births'])

# 【数据初步统计/处理】
# 组装所有txt文件
years = range(1880, 2011)  # 1880-2010年的txt文件
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = r'pydata-book-2nd-edition\datasets\babynames\yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, axis=0, ignore_index=True)  # 不保留读取每个csv文件时返回的原始行号

# 查看各年份男女婴的出生数
total_births = names.pivot_table(index='year', columns='sex', values='births',
                                 aggfunc='sum')  # 生成透视表：行为“年”，列为“性别”，值为“出生数”，统计方式为“求和”
total_births.plot(title='Total births by sex and year')  # 绘制图像

# 统计指定名字的出生数在某年某性别中所占的比例
def add_prop(group):
    births = group.births  # 如果为Python3以下版本，则需要执行此语句，先将births字段转为float格式后计算
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(
    add_prop)  # 按year（年份）和sex（性别）分组后统计。即，统计某个名字的出生数在某年某性别中所占的比例（分子为该名字的出生数，分母为names.groupby(['year', 'sex']).sum()）。
np.allclose(names.groupby(['year', 'sex']).prop.sum(),
            1)  # 检查每个分组的prop值的总和是否等于或近似为1（allclose的默认相对容差参数为1.e-5，即默认误差为1.e-5）

# 取出每个year/sex对的出生数前1000个名字
# 法1：先定义函数，再用apply应用函数
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)  # 对每个year/sex对，取出生数前1000的名字
# 法2：直接使用for循环语句
pieces = []
for year, group in names.groupby(['year', 'sex']):  # 此时year为year/sex对（如(2010, 'M')），group为year/sex对所对应的数据
    pieces.append(group.sort_values(by='births', ascending=False)[:1000])  # 对每个year/sex对中的数据按出生数births倒序排列，取前1000个
top1000 = pd.concat(pieces, ignore_index=True)  # 组合每个year/sex对各自前1000的数据
top1000.to_csv(r'pydata-book-2nd-edition\datasets\babynames\top1000.txt', index=False, sep='|')
top1000 = pd.read_csv(r'pydata-book-2nd-edition\datasets\babynames\top1000.txt', sep='|')



# 【分析命名趋势】
# 分成男女两个部分
boys = top1000.loc[top1000.sex == 'M']
girls = top1000.loc[top1000.sex == 'F']
#
total_births = top1000.pivot_table(index='year', columns='name', values='births',
                                   aggfunc='sum')  # 生成透视表
subset = total_births[['John', 'Harry', 'Marry', 'Marilyn']]  # 取其中一个小数据集
subset.plot(subplots=True, figsize=(12, 20), grid=False,
            title='Number of births by name per year')  # 以子图形式展示（subplots=True），不显示网格（grid=False）
