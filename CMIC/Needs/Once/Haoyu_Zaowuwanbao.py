import pandas as pd
import numpy as np
import random

# 待剔除号码
msg_data = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\zhy_native_msg_basic.txt',
                       sep='|', header=None,
                       names=['month', 'mobileno', 'msg', 'fmt'])
msg_data['mobileno'] = msg_data['mobileno'].astype('str')

# 需剔除号码1：敏感号码（含腾讯在线文档免打扰、特定省份敏感号码）
data_num_mingan = pd.read_excel(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\和飞信免打扰黑名单库.xlsx',
                                header=None,
                                usecols=[1], names=['mobileno'])
# data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag'] = 1

# 需剔除号码2：内部员工号码（含中国移动、特定省份号码）
data_num_jituan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\集团内部号码(2月已处理).csv',
                              header=None, skiprows=1,
                              names=['mobileno'])
# data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 1

# 需剔除号码3：2019年不再下发的120W号码
data_num_120W = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\今年不再发短信的120w号码.csv',
                            header=None, skiprows=1,
                            names=['mobileno'])
data_num_120W['tag'] = 1

# 执行剔除操作
Result = pd.merge(msg_data, data_num_120W,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[Result['tag'] != 1]
msg_data = Result.iloc[:, :4].copy()
# Result['mobileno'] = Result['mobileno'].astype(np.int64)

# 剔除此前已发送过的号码
Result = Result.iloc[:, :4].copy()
data_yfs = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\待剔除汇总.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_yfs['tag'] = 1
Result = pd.merge(Result, data_yfs,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[(Result['tag'] != 1)]
Result = Result.iloc[:, :4].copy()

# 号码有效性检验
Result = Result.loc[Result['mobileno'].map(lambda x: len(str(x)) == 11)]
Result = Result.loc[Result['mobileno'].map(lambda x: str(x)[0] == '1')]
Result.to_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\【9、10月消息量-基础数据】（剔除完成）.txt',
              sep='|', header=None, index=False)

# 读取原始数据（已剔除完成）
Result = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\用户分群结果&原始数据\【8、9月消息量-基础数据】（剔除完成）.txt',
                   sep='|', header=None, names=['month', 'mobileno', 'msg', 'fmt'])

# 匹配最新一天日活
act_data = pd.read_csv(
    r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\native_active_1111.txt',
    sep='|', header=None, names=['mobileno'])
Result = pd.merge(Result, act_data, how='inner', on='mobileno')
Result.iloc[:, :4].to_csv(
    r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\【9、10月消息量-基础数据】（剔除完成）-匹配1111日活.txt',
    sep='|', header=None, index=False)

# 符合条件用户
Result10 = Result.loc[Result['month'] == 201910]
tmp = Result10.loc[(Result10['msg'] >= 24) | (Result10['fmt'] >= 1)]['mobileno']  # 1、重要价值
tmp = Result10.loc[(Result10['msg'] >= 8) & (Result10['msg'] <= 23)]['mobileno']  # 2、一般价值
tmp = Result10.loc[(Result10['msg'] >= 1) & (Result10['msg'] <= 7)]['mobileno']  # 3、一般发展

# 法1
tmp = Result.loc[((Result['month'] == 201909) & ((Result['msg'] >= 24) | (Result['fmt'] >= 1))) | (
        (Result['month'] == 201910) & (Result['msg'] == 0))]  # 4、重要挽留
tmp.loc[tmp.duplicated(subset='mobileno'), 'mobileno'].count()
tmp = tmp.loc[tmp.duplicated(subset='mobileno')]['mobileno']
# 法2
a1 = Result.loc[(Result['month'] == 201909) & ((Result['msg'] >= 24) | (Result['fmt'] >= 1))]
a2 = Result.loc[(Result['month'] == 201910) & (Result['msg'] == 0)]
tmp = pd.merge(a1, a2, how='inner', on='mobileno')['mobileno']

tmp = Result.loc[((Result['month'] == 201909) & ((Result['msg'] >= 8) & (Result['msg'] <= 23))) | (
        (Result['month'] == 201910) & (Result['msg'] == 0))]  # 5、一般挽留
tmp.loc[tmp.duplicated(subset='mobileno'), 'mobileno'].count()
tmp = tmp.loc[tmp.duplicated(subset='mobileno')]['mobileno']

Result2 = Result[['mobileno', 'msg', 'fmt']]
Result910 = Result2.groupby(by='mobileno').sum()
Result910.reset_index(inplace=True)
tmp = Result910.loc[Result910['msg'] == 0]['mobileno']  # 7、历史无需求

tmp = Result.loc[((Result['month'] == 201909) & ((Result['msg'] >= 1) & (Result['msg'] <= 7))) | (
        (Result['month'] == 201910) & (Result['msg'] == 0))]  # 8、流失用户
tmp.loc[tmp.duplicated(subset='mobileno'), 'mobileno'].count()
tmp = tmp.loc[tmp.duplicated(subset='mobileno')]['mobileno']


# 输出符合条件的5W用户包
tmp = tmp.sample(50000)
tmp.to_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\8-流失用户.txt',
           header=None, index=False)

tmp = pd.read_csv(r'C:\Users\Administrator\Desktop\zhy_native_new_active_1007.txt',
                  header=None, names=['mobileno'])

# 匹配最新一天日活
act_data = pd.read_csv(
    r'C:\Users\Administrator\Desktop\native_active_1011.txt',
    sep='|', header=None, names=['mobileno'])
tmp = pd.merge(tmp, act_data, how='inner', on='mobileno')