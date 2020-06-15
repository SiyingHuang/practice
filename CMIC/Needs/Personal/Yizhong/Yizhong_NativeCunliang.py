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
hfx_data = pd.read_csv(path2, header=None, names=['mobileno'])  # SQL提取数据
hfx_data = pd.read_csv(r'C:\Users\Administrator\Desktop\DATA_FUSI_REGISTER_USER_D_0_2_20191110.txt',  # 分析平台下载
                       sep='|', usecols=[6], names=['mobileno'], skiprows=1)
hfx_data.drop_duplicates(inplace=True)
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
# (1)号段表1
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\号段表-1023更新.csv'  # 号段表
data_section_prov = pd.read_csv(path3, header=None,
                                sep=',',
                                encoding='utf-8',
                                usecols=[0, 2, 3, 4], names=['section_no', 'prov', 'city', 'operator'], skiprows=1,
                                dtype={'section_no': np.int32})
# data_section_prov = data_section.loc[data_section['section_no'].notna()]  # 去除空值（存在省份为其他、中国，而section_no为空的情况）
# data_section_prov['section_no'] = data_section_prov['section_no'].astype(np.int32)
# (2)号段表2
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\DIM_SECTION_NO_DAY_0610.txt'
data_section_prov = pd.read_csv(path3, header=None, names=['prov', 'city', 'sec'], dtype={'sec': np.int32})

path4 = r'C:\Users\Administrator\Desktop\huawei_poten_0612.txt'
data = pd.read_csv(path4, header=None, names=['mobileno'])  # 源数据（完成剔除后）
data = pd.read_csv(r'C:\Users\Administrator\Desktop\native_zd_statistics.txt', header=None,
                   names=['date', 'sec', 'cnts'], dtype={'sec': np.int32})
data = data.loc[data.sec.notna()]
data['sec'] = data['mobileno'].map(lambda x: str(x)[:7]).astype(np.int32)
# 源数据匹配号段表
data_section_prov['tag'] = 1
data_tmp = pd.merge(data, data_section_prov,
                    how='left',
                    on='sec')
data_tmp['tag'] = data_tmp.tag.fillna('2')
data_tmp.loc[data_tmp.tag == '2']
data_tmp.groupby(by=['date']).sum()['cnts']
data_tmp2 = data_tmp.loc[data_tmp.prov.isin(['广东'])]
data_tmp2.groupby(by=['date', 'prov']).sum()['cnts']
data_tmp2.groupby(by=['date', 'tag']).sum()['cnts'].to_excel(r'C:\Users\Administrator\Desktop\test.xlsx')
# 筛选出所需省份用户
data = data_tmp.loc[data_tmp['prov'] == '湖北'][['mobileno']]
data_tmp.loc[data_tmp['prov'] == '湖北'][['mobileno']].to_csv(r'C:\Users\Administrator\Desktop\华为潜在用户-湖北.txt',
                sep='|', header=None, index=False)
data_tmp['prov'].value_counts()
data_tmp.iloc[:, [0, 3, 4]].to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\huawei_new_（各省份）_1118和飞信.txt',
                                   sep='|', header=None, index=False)



del data, tmp
# 【已预处理数据，取出分省数据】
# 已剔除数据
with open(path1) as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
brand = 'huawei9'
brand = 'huawei_new'
brand = 'MIUI10'
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_1124和飞信.txt'.format(brand)
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_0106和飞信_120W.txt'.format(brand)
data = pd.read_csv(path1, sep='|', header=None, skiprows=0, names=['mobileno', 'prov', 'city'], encoding='utf-8')
brand = 'xiaomi'
data = pd.read_csv(path1, sep='|', header=None, skiprows=0, names=['mobileno', 'prov'], encoding='utf-8')

# 剔除和飞信注册用户
hfx_date = '20200106'
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\ANDFETION_REGISTER_{}.txt'.format(hfx_date)
hfx_data = pd.read_csv(path2, header=None, names=['mobileno'])
hfx_data = pd.read_csv(r'C:\Users\Administrator\Desktop\DATA_FUSI_REGISTER_USER_D_0_2_20191110.txt',  # 分析平台下载
                       sep='|', usecols=[6], names=['mobileno'], skiprows=1)
hfx_data.drop_duplicates(inplace=True)  # 只有分析平台下载的和飞信注册用户，才需要完成去重操作
hfx_data['tag1'] = 1
tmp = pd.merge(data, hfx_data, how='left', on='mobileno')
tmp.loc[tmp['tag1'] == 1]
tmp = tmp.loc[tmp['tag1'] != 1]

# 输出号码、省份、地市共3个字段
tmp = data_num_except.copy()
tmp.iloc[:, :3].to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_{}和飞信.txt'.format(brand, hfx_date[-4:]),
    sep='|', header=None, index=False)
tmp.iloc[:, :3].to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_{}和飞信_120W.txt'.format(brand, hfx_date[-4:]),
    sep='|', header=None, index=False)
# 仅输出号码字段
tmp.iloc[:, 0].to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_（各省份）_{}和飞信.txt'.format(brand, hfx_date[-4:]),
    sep='|', header=None, index=False)

# 输出分省号码包
prov_name = '四川'
(tmp.loc[tmp['prov'] == '湖北'][['mobileno']]).to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_{}.txt'.format(brand, prov_name),
    header=None, index=False)
(data.loc[data['prov'] == '四川'][['mobileno']]).to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_{}.txt'.format(brand, prov_name),
    header=None, index=False)
tmp1 = data.loc[(data['prov'] != '河北') & (data['prov'] != '北京') & (data['prov'] != '安徽')][['mobileno']]
tmp1['mobileno'] = tmp1['mobileno'].astype('str')+'@139.com'
tmp1.to_csv(
    r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\{}_0106.txt'.format(brand),
    header=None, index=False)

# 合并huaewi9和huawei_new两个号码包
data1 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\huawei9_四川.txt',
                    header=None, names=['mobileno'])
data2 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\huawei_new_四川.txt',
                    header=None, names=['mobileno'])
data1 = data1.append(data2)
data1.drop_duplicates().to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\一众\剔除（和飞信+敏感）结果\huawei_四川.txt',
                               header=None, index=False)
