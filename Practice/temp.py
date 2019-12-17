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



data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191104003_gb_maap_1104.txt',
                   sep='|', header=None, usecols=[6], names=['mobileno'])
data.drop_duplicates()
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\maap_GB_day_active_period_D_20191104.txt',
                   sep='|', header=None, usecols=[8], names=['mobileno'])
data2.drop_duplicates()
set(data2['mobileno'])-set(data['mobileno'])


with open(r'C:\Users\Administrator\Desktop\DATA_FUSI_ACTIVE_USER_M_0_4_201911.txt',
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





data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\20191208_I_DATA_CHATBOT_USER_DTL_D.txt',
                              sep='|', header=None, usecols=[1, 7, 8], names=['mobileno', 'prov', 'city'],
                              skiprows=1)

data_num_except = pd.read_excel(r'C:\Users\Administrator\Desktop\魅族国标用户提数需求及Native发送用户活跃用户匹配需求\上海下发消息（289199）.xlsx',
                                header=None, names=['mobileno', 'prov', 'city'])
native_act = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_1208.txt',
                         sep='|', header=None, names=['mobileno'], usecols=[0])
native_act = native_act.dropna()
native_act['mobileno'] = native_act['mobileno'].astype(np.int64)
Result = pd.merge(data_num_except, native_act, how='inner', on='mobileno')
Result.to_excel(r'C:\Users\Administrator\Desktop\魅族国标用户提数需求及Native发送用户活跃用户匹配需求\上海下发消息（289199）（已匹配1208Native日活）.xlsx',
                header=None, index=False)

data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\结算明细\限制首月活跃晚于新增\最终保存明细-20191210\MI_201812(mobileno&imei_drop_duplicates)-3441287.txt',
                   sep='|', header=None)
data.iloc[:, [0, 1, 2, 3]].to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\结算明细\限制首月活跃晚于新增\最终保存明细-20191210\MI_201812_normal(3441287).txt',
    sep='|', header=None, index=False)






data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_1214.txt',
                   sep='|', header=None, names=['mobileno', 'brand'])
data = data.loc[data['mobileno'].notna()]
data['mobileno'] = data['mobileno'].astype(np.int64)
data['brand'].value_counts()
data['tag'] = 1

data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\合并结果_2558847.txt',
                    header=None, names=['mobileno'])

Result = pd.merge(data2, data, how='left', on='mobileno')
Result.loc[Result['tag'] == 1]
Result.loc[Result['tag'] == 1, 'brand'].value_counts()
Result.loc[Result['tag'] == 1, ['mobileno', 'brand']].to_csv(r'C:\Users\Administrator\Desktop\合并结果_2558847（匹配后）.txt',
                                                             sep='|', header=None, index=False)