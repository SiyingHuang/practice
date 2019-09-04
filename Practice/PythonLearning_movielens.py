import pandas as pd

with open(
        r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\movielens\movies.dat') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']  # 用户信息
users = pd.read_table(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\movielens\users.dat',
    sep='::', header=None, names=unames, engine='python')
mnames = ['movie_id', 'title', 'genres']  # 电影信息
movies = pd.read_table(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\movielens\movies.dat',
    sep='::', header=None, names=mnames, engine='python')
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']  # 评分
ratings = pd.read_table(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\movielens\ratings.dat',
    sep='::', header=None, names=rnames, engine='python')
# 合并数据
data = pd.merge(pd.merge(users, ratings), movies)
data.iloc[:3]  # iloc把3视为位置position，取出前3行数据
data.loc[:3]  # loc把3视为索引的标签label，从第一行开始取至索引标签为3的4行数据
data.ix[0]  # 优先基于索引的标签loc，若不存在标签则会回退到iloc