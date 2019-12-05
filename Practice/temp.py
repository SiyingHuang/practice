import pandas as pd
import numpy as np
import os
import random
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs.txt',
                     header=None, usecols=[0], names=['mobileno'])
data = data.drop_duplicates()
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_0908.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])
# data2 = data2.drop_duplicates()
data2['tag'] = 1
Result = pd.merge(data, data2, how='left', on='mobileno')
Result = Result.loc[Result['tag'] == 1]
Result['mobileno'].to_csv(
    r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs（匹配后）.txt',
    header=None, index=False)



data = pd.read_csv(r'C:\Users\Administrator\Desktop\请协助提数-邮箱超服拉新第二批（1400万）\huawei9_0818_fjm_16to27.txt',
                   header=None, names=['mobileno'])
data['mobileno'] = data['mobileno'].map(lambda x: str(x)[:11])
data['mobileno'] = data['mobileno'].astype(np.int64)
data['tag'] = '1'
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\请协助提数-邮箱超服拉新第二批（1400万）\MIUI10_0818_fjm_11to12.txt',
                   header=None, names=['mobileno'])
data2['mobileno'] = data2['mobileno'].map(lambda x: str(x)[:11])
data2['mobileno'] = data2['mobileno'].astype(np.int64)
data2['tag'] = '2'
data = data.append(data2)
data.drop_duplicates()

new_data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_1014to1018.txt\native_new_1014to1018.txt',
                       header=None, names=['mobileno'])
new_data['if_new'] = 1

Result = pd.merge(data, new_data, how='left', on='mobileno')
Result.to_csv(r'C:\Users\Administrator\Desktop\请协助提数-邮箱超服拉新第二批（1400万）\号码汇总.txt',
              sep='|', header=None, index=False)

data['tag'].value_counts()
Result['tag'].value_counts()

Result.loc[Result['tag'] == '2', 'mobileno'].to_csv(r'C:\Users\Administrator\Desktop\请协助提数-邮箱超服拉新第二批（1400万）\MIUI10_0818_fjm_16to27（新增号码）.txt',
                                                    header=None, index=False)

tmp = pd.read_csv(r'C:\Users\Administrator\Desktop\test.txt',
                  header='infer')



data11201 = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191104003_gb_maap1031.txt',
                        sep='|', header=None)
data11201['imei'] = data11201.iloc[:, 12].map(lambda x: str(x)[14:])
data11201['section_no'] = (data11201.iloc[:, 6].map(lambda x: str(x)[:7])).astype(np.int32)

data11201.iloc[:, 6]

hd_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\号段表-1023更新.csv',
                      header=None, skiprows=1, usecols=[0, 2, 3], names=['section_no', 'prov', 'city'])

Result = pd.merge(data11201, hd_data, how='inner', on='section_no')

Result.drop(columns='section_no', inplace=True)

Result.to_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191104003_gb_maap1031（省份、地市）.txt',
              header=None, index=False)


data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191104003_gb_maap_1104.txt',
                   sep='|', header=None, usecols=[6], names=['mobileno'])
data.drop_duplicates()
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\maap_GB_day_active_period_D_20191104.txt',
                   sep='|', header=None, usecols=[8], names=['mobileno'])
data2.drop_duplicates()
set(data2['mobileno'])-set(data['mobileno'])


with open(r'C:\Users\Administrator\Desktop\DATA_FUSI_REGISTER_USER_D_0_2_20191110.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

tmp = pd.read_excel(r'C:\Users\Administrator\Desktop\native端口号内容运营“飞闻快报”内测阶段目标号码\星座运势第三批订阅号码.xls',
                    sheet_name=1)

count = 0
f = open(r'C:\Users\Administrator\Desktop\hxmz_active_period_M_201909\hxmz_active_period_M_meizu_cunliang_201909.txt',
         encoding='utf-8')
for line in f.readlines():
    count = count+1
print(count)





data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_no_app_active_recent_30_days.txt',
                   header=None, sep='|', usecols=[0, 1, 2, 3], names=['mobileno', 'prov', 'city', 'brand'])
data.dropna(subset=['mobileno'], inplace=True)
data['mobileno'] = data['mobileno'].astype(np.int64)

data_num_jituan_cmp = pd.read_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树[公司+号码]（剔除疑似异常号码）.csv',  # 带公司名
    header=None, names=['cmp', 'mobileno'])
data_num_jituan = pd.read_csv(r'集团内部号码(2月已处理).csv',
                              header=None, skiprows=1,
                              names=['mobileno'])
Result = pd.merge(data, data_num_jituan, how='inner', on='mobileno')
Result2 = pd.merge(Result, data_num_jituan_cmp, how='left', on='mobileno')
data_num_except = Result2.copy()

data_num_except['section_no'] = data_num_except['mobileno'].map(lambda x: str(x)[:7])
data_section = data_section.loc[data_section['prov'] != '河北']
data_num_except = data_num_except.iloc[:, :5]
data_num_except = data_num_except.loc[data_num_except['prov'] != '河北']
data_num_except.loc[data_num_except['prov'] == '北京']

data_num_except.to_csv(r'C:\Users\Administrator\Desktop\请协助提取集团内部员工号码.txt',
                       sep='|', header=None, index=False)


data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\huawei_1to21.txt',
                    header=None, names=['mobileno'])
data1['mobileno'] = data1['mobileno'].map(lambda x: str(x)[:11])
data1['mobileno'] = data1['mobileno'].astype(np.int64)
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_1118to1124.txt',
                    header=None, names=['mobileno'])
len(pd.merge(data1, data2, how='inner', on='mobileno'))

data = pd.read_csv(r'C:\Users\Administrator\Desktop\270W小米native潜在用户\270W_xiaomi_miui10(验证).csv',
                   header=None, names=['mobileno', 'prov'], skiprows=1, usecols=[0, 1])
data.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\xiaomi_（各省份）_1201和飞信_120W.txt', sep='|', header=None, index=False)




