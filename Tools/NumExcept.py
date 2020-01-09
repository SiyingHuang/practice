# 对给定的原始数据，剔除指定号码

import pandas as pd
import numpy as np
import os

# 待剔除号码
data_num_except = data.copy()
data_num_except = tmp.iloc[:, :1].copy()
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\请协助提取流失用户数据\native_liushi_20191208.txt',
                              sep='|', header=None,
                              names=['mobileno', 'brand'])
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_1208.txt',
                              sep='|', header=None,
                              names=['mobileno', 'prov', 'brand'])
data_num_except = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\MIUI10_（各省份）_1110和飞信_120W.txt',
                              sep='|', header=None,
                              names=['mobileno', 'prov', 'city'])
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851（匹配12月月活MaaP并剔除后）.txt',
                              header=None, usecols=[0], skiprows=0,
                              names=['mobileno'])
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\DATA_FUSI_ACTIVE_USER_M_0_4_201911.txt',
                              header=None, sep='|', usecols=[5], skiprows=1,
                              names=['mobileno'])
data_num_except = pd.read_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1.xlsx',
                                header=None,
                                names=['mobileno'],
                                encoding='GBK')
# data_num_except['mobileno'] = data_num_except['mobileno'].astype('str')

os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist')  # 切换工作目录
# 需剔除号码1：敏感号码（含腾讯在线文档免打扰、特定省份敏感号码）
data_num_mingan = pd.read_csv(r'和飞信免打扰黑名单库.txt',
                                header=None,
                                usecols=[1], names=['mobileno'], skiprows=1)
# data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag'] = 1

# 需剔除号码2：内部员工号码（含中国移动、特定省份号码）
data_num_jituan = pd.read_csv(r'集团内部号码(2月已处理).csv',
                              header=None, skiprows=1,
                              names=['mobileno'])
# data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 1

# 需剔除号码3：2019年不再下发的120W号码
data_num_120W = pd.read_csv(r'今年不再发短信的120w号码.csv',
                            header=None, skiprows=1,
                            names=['mobileno'])
data_num_120W['tag'] = 1

# 需剔除号码4：移动内部（集团公司、省公司、专业公司）部门及部门以上级别领导号码 --包含在2中
data_num_ld = pd.read_csv(r'集团省专业公司部门及以上&大boss-20191115.txt',
                          header=None, names=['mobileno'])
data_num_ld['tag'] = 1

# 需剔除号码5：已下发1条及以上的不再打扰用户
data_not_disturb = pd.read_csv(r'12月已下发过的号码.txt', header=None, names=['mobileno'], skiprows=1)
data_not_disturb['tag'] = 1

# 执行剔除操作
Result = pd.merge(data_num_except, data_num_120W,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[Result['tag'] != 1]
data_num_except = Result.iloc[:, 0].copy()
data_num_except = Result.iloc[:, :2].copy()
data_num_except = Result.iloc[:, :3].copy()
data_num_except = Result.iloc[:, :5].copy()

Result.iloc[:, 0].to_csv(r'C:\Users\Administrator\Desktop\王者-移动-3246851（匹配12月月活MaaP并剔除后）.txt',
                          sep='|', header=False, index=False)
Result.to_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1（剔除后）.xlsx',
                header=False, index=False)
Result.iloc[:, :3].to_csv(r'C:\Users\Administrator\Desktop\Chatbot日活1208（已剔除）.txt',
                          sep='|', header=False, index=False)
Result.iloc[:, :4].to_csv(r'C:\Users\Administrator\Desktop\native_dayactive_0925to0928.txt',
                          sep='|', header=False, index=False)
data_num_except.to_csv(r'C:\Users\Administrator\Desktop\tmp_20191119001_yz_native_active_no_msg.txt',
                       header=None, index=False)
data_num_except.to_csv(r'C:\Users\Administrator\Desktop\Native十一月份流失用户\十一月份流失用户（剔除完成）.txt',
                       sep='|', header=None, index=False)
data_num_except.loc[data_num_except['brand'] == '华为', ['mobileno', 'prov']].to_csv(
    r'C:\Users\Administrator\Desktop\华为1208日活.txt', sep='|', header=None, index=False)

Result = pd.DataFrame(
    set(data_num_except['mobileno'])
    - set(data_num_mingan['mobileno'])
    - set(data_num_jituan['mobileno'])
    - set(data_num_120W['mobileno'])
    - set(data_not_disturb['mobileno']), columns=['mobileno'])

Result = pd.DataFrame(
    set(data_num_except['mobileno'])
    - set(data_num_mingan['mobileno'])
    - set(data_num_jituan['mobileno'])
    - set(data_num_120W['mobileno']), columns=['mobileno'])