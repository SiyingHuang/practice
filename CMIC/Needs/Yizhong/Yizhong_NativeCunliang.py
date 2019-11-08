import pandas as pd
import numpy as np

# 【原始数据处理】
# 原始数据
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\huawei9（各省份）_1007和飞信.txt'
with open(path1) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(path1,
                   sep='|', header=None, skiprows=0, names=['mobileno', 'prov', 'city'])


# 剔除和飞信注册用户（20190818）
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\andfetion_register_1016.txt'
with open(path2) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
hfx_data = pd.read_csv(path2, header=None, names=['mobileno'])
hfx_data['tag1'] = 1
tmp = pd.merge(data, hfx_data, how='left', on='mobileno')
tmp.loc[tmp['tag1'] == 1]
tmp = tmp.loc[tmp['tag1'] != 1, ['mobileno', 'prov', 'city']]
tmp.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果_0818\huawei9（各省份）_1016和飞信.txt',
           sep='|', header=None, index=False)


# 剔除敏感号码
tmp = pd.merge(tmp, data_num_mingan, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag'] != 1, ['mobileno']]


# 输出剔除结果
tmp.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\MIUI10_0818.txt',
           header=None, index=False)


# 找出指定省份用户
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\号段表-1023更新.csv'  # 号段表
data_section = pd.read_csv(path3, header=None,
                           sep=',',
                           encoding='utf-8',
                           usecols=[0, 2, 3, 4], names=['section_no', 'prov', 'city', 'operator'], skiprows=1)
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




# 【已预处理数据，取出分省数据】
# 已剔除数据
with open(path1) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
brand = 'huawei9'
brand = 'MIUI10'
hfx_date = '1107'
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_1030和飞信.txt'.format(brand)
data = pd.read_csv(path1, sep='|', header=None, skiprows=0, names=['mobileno', 'prov', 'city'], encoding='utf-8')

# 剔除和飞信注册用户
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\andfetion_register_{}.txt'.format(hfx_date)
data_hfx = pd.read_csv(path2, header=None, names=['mobileno'])
data_hfx['tag1'] = 1
tmp = pd.merge(data, data_hfx, how='left', on='mobileno')
tmp.loc[tmp['tag1'] == 1]
tmp = tmp.loc[tmp['tag1'] != 1]

tmp.iloc[:, :3].to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_{}和飞信.txt'.format(brand, hfx_date),
    sep='|', header=None, index=False)
prov_name = '湖北'
(tmp.loc[tmp['prov'] == '四川']['mobileno']).to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_{}.txt'.format(brand, prov_name),
    header=None, index=False)
