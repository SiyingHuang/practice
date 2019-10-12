import pandas as pd
import numpy as np

# 原始数据
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_0818.txt'
with open(path1) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data = pd.read_csv(path1, header=None, skiprows=0, names=['mobileno'])


# 剔除和飞信注册用户（20190818）
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\andfetion_register_1007.txt'
with open(path2) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data_hfx = pd.read_csv(path2, header=None, names=['mobileno'])
data_hfx['tag1'] = 1
tmp = pd.merge(data, data_hfx, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag1'] != 1, ['mobileno']]


# 剔除敏感号码
tmp = pd.merge(tmp, data_num_mingan, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag'] != 1, ['mobileno']]


# 输出剔除结果
tmp.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\MIUI10_0818.txt',
           header=None, index=False)


# 找出指定省份用户
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\DIM_SECTION_NO_DAY_1007.txt'  # 号段表
data_section = pd.read_csv(path3, header=None,
                           sep='|',
                           encoding='utf-8',
                           names=['prov', 'city', 'section_no'])
data_section_prov = data_section.loc[data_section['section_no'].notna()]  # 去除空值（存在省份为其他、中国，而section_no为空的情况）
data_section_prov['section_no'] = data_section_prov['section_no'].astype(np.int32)

path4 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_0818.txt'
data = pd.read_csv(path4, header=None, names=['mobileno'])  # 源数据（完成剔除后）
data['sec'] = data['mobileno'].map(lambda x: str(x)[:7]).astype(np.int32)
# 源数据匹配号段表
data_tmp = pd.merge(data, data_section_prov,
                    how='inner',
                    left_on='sec', right_on='section_no')
# 筛选出所需省份用户
data_tmp.loc[data_tmp['prov'] == '广东']['mobileno'].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_广东（2667416个）_0821号段表.txt',
                sep='|', header=None, index=False)
data_tmp['prov'].value_counts()





# 已剔除数据
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_0818（各省份）_1007和飞信.txt'
with open(path1) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(path1, sep='|', header=None, skiprows=0, names=['mobileno', 'prov', 'city'], encoding='utf-8')

# 剔除和飞信注册用户（20191007）
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\andfetion_register_1007.txt'
data_hfx = pd.read_csv(path2, header=None, names=['mobileno'])
data_hfx['tag1'] = 1
tmp = pd.merge(data, data_hfx, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag1'] != 1]

tmp.iloc[:, :3].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_0818（各省份）_1007和飞信.txt',
           sep='|', header=None, index=False)

(data.loc[data['prov'] == '上海']['mobileno']).to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\huawei9_上海.txt',
                                                  header=None, index=False)


# 需剔除号码1
data_num_mingan = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\敏感号码.txt',
                              sep='|', header=None,
                              names=['mobileno'])
data_num_mingan['tag'] = 1

tmp = pd.merge(data, data_num_mingan, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag'] == '1']

import random
random.sample([1,2,3], 2)