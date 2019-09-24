import pandas as pd

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
data = pd.merge(pd.merge(users, ratings),
                movies)  # 等价于 data = pd.merge(pd.merge(users, ratings, how='inner', on='user_id'), movies, how='inner', on='movie_id')
data.iloc[:3]  # iloc把3视为位置position，取出前3行数据
data.loc[:3]  # loc把3视为索引的标签label，从第一行开始取至索引标签为3的数据
data.ix[0]  # 优先基于索引的标签loc，若不存在标签则会回退到iloc

# 按性别计算每部电影的平均得分
mean_ratings = data.pivot_table(index='title', columns='gender', values='rating', aggfunc='mean')
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]  # 筛选出评分次数>=250次的电影
mean_ratings = mean_ratings.loc[active_titles]  # active_titles是Index，可用loc取索引在active_titles是Index中的值。
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

# 计算评分分歧
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[::-1]  # 倒序，相当于sorted_by_diff[-1:-len(sorted_by_diff)-1:-1]。
# 找出分歧最大的电影（不考虑性别）
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]  # 筛选出评分次数>=250次的电影
rating_std_by_title.sort_values(ascending=False)[:10]