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

# 需剔除号码1：敏感号码
data_num_mingan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\敏感号码.txt',
                              sep='|', header=None,
                              names=['mobileno'])
# data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag'] = 2

# 需剔除号码2：中国移动集团内部员工号码
data_num_jituan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树.txt',
                              sep='|', header=None,
                              names=['mobileno'])  # 号码已预处理，加载后为int64格式
# data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 2

# 需剔除号码3：集团领导信息
data_num_jituan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\集团领导信息.txt',
                              sep=',', header=None,
                              names=['names', 'mobileno', 'group'])
data_num_jituan.loc[data_num_jituan['mobileno'].map(lambda x: len(str(x)) == 11)]
data_num_jituan['tag'] = 2

# 执行剔除操作
Result = pd.merge(data_num_except, data_num_jituan,
                  how='left',
                  on='mobileno')
tmp = Result.loc[Result['tag'] == 2]
len(tmp['mobileno'].drop_duplicates())
Result = Result.loc[Result['tag'] != 2]
Result['mobileno'] = Result['mobileno'].astype(np.int64)
Result = pd.DataFrame(Result).drop_duplicates().astype(np.int64)

Result.iloc[:, 0].to_csv(r'C:\Users\Administrator\Desktop\【剔除后结果】native_dayactive_0928to1016.txt',
                          sep='|', header=False, index=False)
Result.to_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1（剔除后）.xlsx',
                header=False, index=False)

Result.iloc[:, :4].to_csv(r'C:\Users\Administrator\Desktop\native_dayactive_0925to0928.txt',
                          sep='|', header=False, index=False)
