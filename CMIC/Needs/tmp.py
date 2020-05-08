# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import os
import random
import datetime

with open(
        r'C:\Users\Administrator\Desktop\黑名单.txt',
        encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

count = 0
f = open(r'C:\Users\Administrator\Desktop\20191230_I_DATA_CHATBOT_USER_DTL_D.txt',
         encoding='utf-8')
for line in f.readlines():
    count = count + 1
print(count)

# 原始数据
data = pd.read_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户.txt', header=None, sep='&&',
                   names=['mobileno'], usecols=[1], skiprows=1)
# 全量国标MaaP活跃
gb = pd.read_csv(r'C:\Users\Administrator\Desktop\20191217_I_DATA_CHATBOT_USER_DTL_D.txt',
                 sep='|', header=None, skiprows=1, usecols=[1], names=['mobileno'])
# 全量国标MaaP活跃（剔除魅蓝用户）
gb_no_mz = pd.read_csv(r'C:\Users\Administrator\Desktop\gb_maap_active_1217.txt', header=None, names=['mobileno'])
# 全量Native活跃
native = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_gd_1217.txt', header=None, names=['mobileno'])
# 全量Native活跃（剔除全量国标MaaP用户）
native_no_gb = pd.DataFrame(set(native['mobileno']) - set(gb['mobileno']), columns=['mobileno'])

tmp1 = pd.merge(data, native_no_gb, how='inner', on='mobileno')
tmp1.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（native非国标）.txt', header=None, index=False)

tmp2 = pd.merge(data, gb_no_mz, how='inner', on='mobileno')
tmp2.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（国标非魅蓝）.txt', header=None, index=False)

tmp3 = pd.DataFrame(set(data['mobileno']) - set(tmp1['mobileno']) - set(tmp2['mobileno']), columns=['mobileno'])
tmp3.to_csv(r'C:\Users\Administrator\Desktop\10月超套0至20元客户\10月超套0至20元客户（剩余号码）.txt', header=None, index=False)

chk1 = pd.read_csv(r'C:\Users\Administrator\Desktop\需剔除1219\需剔除\第五批\华为_2.txt', header=None, names=['mobileno'],
                   skiprows=0)
chk2 = pd.read_csv(r'C:\Users\Administrator\Desktop\受影响的1375用户.txt', sep='|', header=None, usecols=[0],
                   names=['mobileno'], skiprows=1)
pd.DataFrame(set(chk1['mobileno']) - set(chk2['mobileno'])).to_csv(
    r'C:\Users\Administrator\Desktop\需剔除1219\需剔除\第五批\华为_2.txt',
    header=None, index=False)

reader = pd.read_csv(r'D:\yy_1252004012520040123_and_12520040123_1220to1224.txt',
                     sep='|', header=None, chunksize=100000)
tmp = []
for chunk in reader:
    chunk.rename(columns={24: 'statis_hour'}, inplace=True)
    chunk['date'] = chunk['statis_hour'].map(lambda x: str(x)[:8])
    tmp = pd.concat((pd.DataFrame(tmp), chunk.loc[chunk['date'] == '20191220']))

act = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_zhaohui.txt',
                  header=None, names=['mobileno'])
ori = pd.read_csv(r'C:\Users\Administrator\Desktop\核对1219\核对\剔除后全量.txt', header=None, sep='|',
                  names=['mobileno', 'brand'])
minus = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist\受影响的1375用户.txt', header=None,
                    names=['mobileno'], skiprows=1)  # 待剔除号码
ori = pd.merge(ori, pd.DataFrame(set(ori['mobileno']) - set(minus['mobileno']),
                                 columns=['mobileno']), how='inner', on='mobileno')  # 剔除后
len(set(ori['mobileno']) - set(minus['mobileno']))
Result = pd.merge(act, ori, how='inner', on='mobileno')
Result['brand'].value_counts()

s = pd.Series(['a', 'b', 'c'], name='num')
s.to_frame()


def fun(ls: list, s: int) -> list:
    ls.to_csv()
    s.lower()

    return '123'



os.chdir(r'C:\Users\Administrator\Desktop')

path = r'hfx_origin_sso_web.txt'
path = r'hfx_origin_message_storage_web.txt'
path = r'zhushanzhi_0507.txt'

with open(path, encoding='gbk') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_name_list = list(('adate', 'log_level', 'class', 'controller', 'member_function', 'remote_addr', 'x_real_id', 'x_forward_for', 'http_method', 'http_uri', 'user_agent', 'session', 'auser', 'duration', 'result', 'message', 'dtime'))

data = pd.read_csv(path, header=None, sep='|',
                   names=data_name_list)
data = pd.read_csv(path, header=None, sep='|',
                   names=['adate', 'result', 'duration', 'user_agent'],
                   dtype={'user_agent': 'str'}, encoding='utf-8',
                   parse_dates=[0])
data.iloc[:, [0]]


black_list = pd.read_csv(r'C:\Users\Administrator\Desktop\黑名单.txt',
                         header=None, names=['mobileno'],
                         sep='&&', usecols=[0], engine='python', dtype={'mobileno': 'str'},
                         chunksize=100000)
bl = []
for i in black_list:
    bl.append(i)

result = pd.concat(bl, ignore_index=True)

result.loc[(result.mobileno.map(lambda x: len(str(x)) != 11)) | (~result.mobileno.map(lambda x: str(x).startswith('1')))]
result = result.loc[(result.mobileno.map(lambda x: len(str(x)) == 11)) & (result.mobileno.map(lambda x: str(x).startswith('1')))]

result.to_csv(r'黑名单处理后.txt', index=False)


# 承宗提供的脚本
from preprocess.data_handler import DataHandler

data = pd.read_csv(r'C:\Users\Administrator\Desktop\chatbot_day_active_gd_mz_0426.txt',
                   header=None, names=['mobileno', 'city'], usecols=[0, 1])
dh = DataHandler(data=data)
dh.delete_blacklist()
dh.delete_staff()
result = dh.save()
result = pd.merge(result, data, how='left', on='mobileno')
result.to_csv(r'C:\Users\Administrator\Desktop\chatbot_day_active_gd_mz_0426（已剔除）.txt',
              header=None, index=False)
