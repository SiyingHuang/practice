import pandas as pd
import numpy as np
import os
import random
import datetime

with open(r'C:\Users\Administrator\Desktop\20191230_I_DATA_CHATBOT_USER_DTL_D.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

count = 0
f = open(r'C:\Users\Administrator\Desktop\20191230_I_DATA_CHATBOT_USER_DTL_D.txt',
         encoding='utf-8')
for line in f.readlines():
    count = count+1
print(count)


# 原始数据
data = pd.read_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户.txt', header=None, sep='&&', names=['mobileno'], usecols=[1], skiprows=1)
# 全量国标MaaP活跃
gb = pd.read_csv(r'C:\Users\Administrator\Desktop\20191217_I_DATA_CHATBOT_USER_DTL_D.txt',
                   sep='|', header=None, skiprows=1, usecols=[1], names=['mobileno'])
# 全量国标MaaP活跃（剔除魅蓝用户）
gb_no_mz = pd.read_csv(r'C:\Users\Administrator\Desktop\gb_maap_active_1217.txt', header=None, names=['mobileno'])
# 全量Native活跃
native = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_gd_1217.txt', header=None, names=['mobileno'])
# 全量Native活跃（剔除全量国标MaaP用户）
native_no_gb = pd.DataFrame(set(native['mobileno'])-set(gb['mobileno']), columns=['mobileno'])

tmp1 = pd.merge(data, native_no_gb, how='inner', on='mobileno')
tmp1.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（native非国标）.txt', header=None, index=False)

tmp2 = pd.merge(data, gb_no_mz, how='inner', on='mobileno')
tmp2.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（国标非魅蓝）.txt', header=None, index=False)

tmp3 = pd.DataFrame(set(data['mobileno'])-set(tmp1['mobileno'])-set(tmp2['mobileno']), columns=['mobileno'])
tmp3.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（剩余号码）.txt', header=None, index=False)

chk1 = pd.read_csv(r'C:\Users\Administrator\Desktop\需剔除1219\需剔除\第五批\华为_2.txt', header=None, names=['mobileno'],
                   skiprows=0)
chk2 = pd.read_csv(r'C:\Users\Administrator\Desktop\受影响的1375用户.txt', sep='|', header=None, usecols=[0],
                   names=['mobileno'], skiprows=1)
pd.DataFrame(set(chk1['mobileno'])-set(chk2['mobileno'])).to_csv(r'C:\Users\Administrator\Desktop\需剔除1219\需剔除\第五批\华为_2.txt',
                                                                 header=None, index=False)





os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist')
data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191230001_qy_native_msg_day.txt',
                   sep='|', header=None, skiprows=0, names=['date', 'mobileno', 'mess_cnt'])
data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191230001_qy_native_msg_month12.txt',
                   sep='|', header=None, skiprows=0, names=['mobileno', 'mess_cnt'])
data = data.loc[~(data['mess_cnt'] == 0)]
data.to_csv(r'native_msg_count_day.txt', header=None, sep='|')
data2 = pd.read_csv(r'')
data_ld = pd.read_csv(r'集团&专业公司-部门级别以上领导-20191101.txt',
                      header=None, names=['name', 'mobileno', 'prov', 'part', 'level', 'tag'], usecols=[0, 1, 2, 3, 4, 5])
data_num_jituan = pd.read_csv(r'集团内部号码(2月已处理).csv',
                              header=None, skiprows=1,
                              names=['mobileno'])
# data_ld['tag'].value_counts()
# data_ld = data_ld.loc[data_ld['tag'] != 50]
Result = pd.merge(data, data_ld, how='inner', on='mobileno')
Result.to_csv(r'day_ld.txt', header=None, index=False)
Result.to_csv(r'month12_ld.txt', header=None, index=False)

Result['prov'].value_counts().to_csv(r'result.txt', header=None)
data_ld[data_ld['mobileno'].duplicated()]
data_ld = data_ld.sort_values(by=['mobileno', 'prov'])
data_ld.drop_duplicates(inplace=True)
Result = pd.merge(data, data_ld, how='inner', on='mobileno')
Result['prov'].value_counts().to_csv(r'result.txt', sep='|')
Result.to_excel(r'tmp.xlsx')
Result.loc[Result[1] == 201911, 'prov'].value_counts().to_csv(r'result_201911.txt', header=None)






reader = pd.read_csv(r'D:\yy_1252004012520040123_and_12520040123_1220to1224.txt',
                     sep='|', header=None, chunksize=100000)
tmp = []
for chunk in reader:
    chunk.rename(columns={24: 'statis_hour'}, inplace=True)
    chunk['date'] = chunk['statis_hour'].map(lambda x: str(x)[:8])
    tmp = pd.concat((pd.DataFrame(tmp), chunk.loc[chunk['date'] == '20191220']))





act = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_zhaohui.txt',
                  header=None, names=['mobileno'])
ori = pd.read_csv(r'C:\Users\Administrator\Desktop\核对1219\核对\剔除后全量.txt', header=None, sep='|', names=['mobileno', 'brand'])
minus = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\受影响的1375用户.txt', header=None,
                    names=['mobileno'], skiprows=1)  # 待剔除号码
ori = pd.merge(ori, pd.DataFrame(set(ori['mobileno']) - set(minus['mobileno']),
                                 columns=['mobileno']), how='inner', on='mobileno')  # 剔除后
len(set(ori['mobileno']) - set(minus['mobileno']))
Result = pd.merge(act, ori, how='inner', on='mobileno')
Result['brand'].value_counts()