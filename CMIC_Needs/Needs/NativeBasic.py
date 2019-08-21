import pandas as pd

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_new_basic_0731.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_native_basic = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_new_basic_0731.txt',
    sep='|', header=None, usecols=[0, 1], names=['new_date', 'mobileno'])
data_native_basic = data_native_basic.sort_values(by='new_date').drop_duplicates(subset='mobileno',
                                                                                 keep='first')  # 保留号码最早一条新增记录
# 【统计新增用户数】
# 按天统计
tmp = data_native_basic.groupby(['new_date']).count()  # 方式1
tmp2 = data_native_basic['new_date'].value_counts().sort_index()  # 方式2（比groupby要更高效）
# 按月统计
tmp_month = tmp.reset_index()
tmp_month['month'] = tmp_month['new_date'].map(lambda x: str(x)[:6])
tmp_month = tmp_month[['month', 'mobileno']].groupby(['month']).sum()

# 检查重复数据（当同时对mobileno,new_date去重时，会存在一个号码有多天的新增记录）
tmp = data_native_basic.loc[data_native_basic.duplicated(subset='mobileno')]
data_0731 = data_native_basic.loc[data_native_basic.new_date == 20190731]
data_native_basic.loc[data_native_basic.mobileno == 17839532173]
