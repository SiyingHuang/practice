import pandas as pd
import numpy as np
import os
import random
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt', encoding='utf-8') as f:
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


