# 需求描述：
# 合并多个txt文件，并标识为不同分组
# 对某一批号码，按天匹配该号码每日Native新增情况

import pandas as pd

# 合并多个txt文件
data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\活动第二批\A组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data1['group'] = 'A'

data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\活动第二批\B组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data2['group'] = 'B'

data3 = pd.read_csv(r'C:\Users\Administrator\Desktop\活动第二批\C组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data3['group'] = 'C'

data4 = pd.read_csv(r'C:\Users\Administrator\Desktop\活动第二批\对照组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'])
data4['group'] = 'D'

data = pd.concat((data1, data2, data3, data4))
data['mobileno'] = data['mobileno'].map(lambda x: str(x)[:11])

# 0813-0819 Native新增用户明细
data_new = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_0813to0819.txt',
                       sep='|', header=None, names=['date', 'mobileno'])
data_new['tag'] = 1
data_new['tag'] = data_new['tag'].astype(np.int32)

# 关联两个表
Result = pd.merge(data, data_new.astype('str'), how='left')
# 将tag为1的转换为int32，减少存储空间
(Result.loc[Result['tag'] == '1'])['tag'] = (Result.loc[Result['tag'] == '1'])['tag'].astype(np.int32)

# 根据group,date分组统计，再将列转为行
Result[['group', 'date', 'tag']].groupby(['group', 'date']).count().unstack()
# 输出每日新增号码明细
Result.loc[(Result['tag'] == '1')].iloc[:, 0:3].sort_values(by=['group', 'date']).to_csv(
    r'C:\Users\Administrator\Desktop\活动第二批\result_all.txt',
    sep='|', header=True, index=False)

tmp = Result[['group', 'date', 'tag']].groupby(['group', 'date']).count().unstack()
tmp.columns = tmp.columns.levels[1]
tmp.to_csv(r'C:\Users\Administrator\Desktop\活动第二批\statistic.txt',
           sep='|')