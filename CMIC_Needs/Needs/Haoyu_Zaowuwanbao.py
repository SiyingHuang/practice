import pandas as pd
import numpy as np
import random

# 待剔除号码
msg_data = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\zhy_native_msg_basic.txt',
                              sep='|', header=None,
                              names=['month', 'mobileno', 'msg', 'fmt'])
msg_data['mobileno'] = msg_data['mobileno'].astype('str')

# 剔除集团内部员工
data_num_jituan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_num_jituan = data_num_jituan['mobileno'].map(lambda x: str(x)[-11:])
data_num_jituan = pd.DataFrame(data_num_jituan)
# 集团号码txt文件中，存在带+86的号码
data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag1'] = 1

# 剔除敏感号码/黑名单
data_num_mingan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\敏感号码.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag2'] = 1

# 剔除集团号码、敏感号码
Result = pd.merge(msg_data, data_num_jituan,
                  how='left',
                  on='mobileno')
Result = pd.merge(Result, data_num_mingan,
                  how='left',
                  on='mobileno')
Result.loc[(Result['tag1'] != 1) & (Result['tag2'] != 1)]
Result.loc[(Result['tag1'] == 1) | (Result['tag2'] == 1)]
Result = Result.loc[(Result['tag1'] != 1) & (Result['tag2'] != 1)][['month', 'mobileno', 'msg', 'fmt']]
Result['mobileno'] = Result['mobileno'].astype(np.int64)

# 剔除此前已发送过的号码
data_yfs = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\待剔除汇总.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_yfs['tag'] = 1
Result = pd.merge(Result, data_yfs,
                  how='left',
                  on='mobileno')
Result = Result.loc[(Result['tag'] != 1)]
Result = Result.iloc[:, :4]

Result = Result.loc[Result['mobileno'].map(lambda x: len(str(x)) == 11)]
Result = Result.loc[Result['mobileno'].map(lambda x: str(x)[0] == '1')]
Result.to_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\【8、9月消息量-基础数据】（剔除完成）.txt',
              sep='|', header=None, index=False)
Result = pd.read_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\用户分群结果&原始数据\【8、9月消息量-基础数据】（剔除完成）.txt',
                   sep='|', header=None, names=['month', 'mobileno', 'msg', 'fmt'])

# 匹配最新一天日活
act_data = pd.read_csv(
    r'C:\Users\Administrator\Desktop\native_active_1011.txt',
    sep='|', header=None, names=['mobileno'])
act_data['tag'] = 1
Result = pd.merge(data, act_data, how='left', on='mobileno')
Result = Result.loc[Result['tag'] == 1]
Result.iloc[:, :4].to_csv(
    r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\【8、9月消息量-基础数据】（剔除完成）-匹配1010月活.txt',
    sep='|', header=None, index=False)

# 符合条件用户
Result9 = Result.loc[Result['month'] == 201909]
tmp = Result9.loc[(Result9['msg'] >= 24) | (Result9['fmt'] >= 1)]['mobileno']  # 1、重要价值
tmp = Result9.loc[(Result9['msg'] >= 8) & (Result9['msg'] <= 23)]['mobileno']  # 2、一般价值
tmp = Result9.loc[(Result9['msg'] >= 1) & (Result9['msg'] <= 7)]['mobileno']  # 3、一般发展

tmp = Result.loc[((Result['month'] == 201908) & ((Result['msg'] >= 24) | (Result['fmt'] >= 1))) & (
        (Result['month'] == 201909) & (Result['msg'] == 0))]  # 4、重要挽留

tmp = Result.loc[((Result['month'] == 201908) & ((Result['msg'] >= 8) & (Result['msg'] <= 23))) & (
        (Result['month'] == 201909) & (Result['msg'] == 0))]  # 5、一般挽留

Result2 = Result[['mobileno', 'msg', 'fmt']]
Result89 = Result2.groupby(by='mobileno').sum()
Result89.reset_index(inplace=True)
tmp = Result89.loc[Result89['msg'] == 0]['mobileno']  # 7、历史无需求

tmp = Result.loc[((Result['month'] == 201908) & ((Result['msg'] >= 1) & (Result['msg'] <= 7))) & (
        (Result['month'] == 201909) & (Result['msg'] == 0))]  # 8、流失用户


# 输出符合条件的5W用户包
tmp = tmp.sample(50000)
tmp.to_csv(r'C:\Users\Administrator\Desktop\native端口号内容运营“早午晚报”内测阶段目标号码\新进入用户.txt',
           header=None, index=False)
