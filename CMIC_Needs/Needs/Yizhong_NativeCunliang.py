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
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\TW_RHTX_REGISTER_USERS_D_0818.txt'
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

# 找出辽宁省用户
# 号段表
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\DIM_SECTION_NO_DAY_0818.txt'
data_section = pd.read_csv(path3, header=None,
                           sep='|',
                           encoding='utf-8',
                           names=['prov', 'city', 'section_no'])
data_section_liaoning = data_section.loc[data_section['prov'] == '辽宁']
data_section_liaoning['section_no'] = data_section_liaoning['section_no'].astype(np.int32)
# 源数据
path4 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\MIUI10_0818.txt'
data = pd.read_csv(path4, header=None, names=['mobileno'])
data['sec'] = data['mobileno'].map(lambda x: str(x)[:7]).astype(np.int32)
# 源数据匹配号段表
data_tmp = pd.merge(data, data_section_liaoning,
                    how='inner',
                    left_on='sec', right_on='section_no')

data_tmp['mobileno'].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\辽宁_0818.txt',
                sep='|', header=None, index=False)