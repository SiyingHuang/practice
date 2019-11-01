# 对原始数据，剔除指定号码

import pandas as pd
import numpy as np

# 待剔除号码
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\native_dayactive_0928to1016.txt',
                              sep='|', header=None,
                              names=['new_data', 'mobileno', 'prov', 'brand'])
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\【请思颖协助】邮箱账单NPS调研号码筛选\附件2：9月和飞信账单群发的阅读用户清单_20190930需求1结果new.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\Native用户8月消息明细\Native用户8月消息明细.txt',
                              sep='|', header=None, usecols=[0], skiprows=1,
                              names=['mobileno'])
data_num_except = pd.read_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1.xlsx',
                                header=None,
                                names=['mobileno'],
                                encoding='GBK')
# data_num_except['mobileno'] = data_num_except['mobileno'].astype('str')

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
Result = pd.merge(data_num_except, data_num_120W,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[Result['tag'] != 1]
data_num_except = Result.iloc[:, :3].copy()

Result.iloc[:, 0].to_csv(r'C:\Users\Administrator\Desktop\【剔除后结果】native_dayactive_0928to1016.txt',
                          sep='|', header=False, index=False)
Result.to_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1（剔除后）.xlsx',
                header=False, index=False)

Result.iloc[:, :4].to_csv(r'C:\Users\Administrator\Desktop\native_dayactive_0925to0928.txt',
                          sep='|', header=False, index=False)
