import pandas as pd
import numpy as np
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



hd_data = pd.read_excel(r'C:\Users\Administrator\Desktop\号段表-1023更新.xlsx',
                        header=None, names=['section_no', 'area_code', 'prov', 'city', 'operator'], skiprows=1)
hd_data.to_csv(r'C:\Users\Administrator\Desktop\号段表-1023更新.csv',
               index=False)