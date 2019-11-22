# 提取周期内流失用户。
# 原始数据字段：号码、品牌。
# 剔除敏感号码、内部号码、不再下发号码。
# 按品牌拆包，仅输出号码字段。

import pandas as pd
import numpy as np

# 【读取原始文件】
# 切换原始文件路径
os.chdir(r'C:\Users\Administrator\Desktop\Native十一月份流失用户')

ls_data = pd.read_csv(r'剔除后全量.txt',
                      sep='|', header=None, names=['mobileno', 'brand'])
# 【剔除异常号码】
ls_data.loc[ls_data['mobileno'].map(lambda x: len(str(x)) != 11)]
ls_data = ls_data.loc[ls_data['mobileno'].map(lambda x: len(str(x)) == 11)]

# 【剔除敏感号码（多类敏感号码）】
os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-号码剔除验证工具\blacklist')
# 需剔除号码1：敏感号码（含腾讯在线文档免打扰、特定省份敏感号码）
data_num_mingan = pd.read_excel(r'和飞信免打扰黑名单库.xlsx',
                                header=None,
                                usecols=[1], names=['mobileno'])
# data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag'] = 1

# 需剔除号码2：内部员工号码（含中国移动、特定省份号码）
data_num_jituan = pd.read_csv(r'集团内部号码(2月已处理).csv',
                              header=None, skiprows=1,
                              names=['mobileno'])
# data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 1

# 需剔除号码3：2019年不再下发的120W号码
data_num_120W = pd.read_csv(r'今年不再发短信的120w号码.csv',
                            header=None, skiprows=1,
                            names=['mobileno'])
data_num_120W['tag'] = 1

# 需剔除号码4：移动内部（集团公司、省公司、专业公司）部门及部门以上级别领导号码
data_num_ld = pd.read_csv(r'集团省专业公司部门及以上&大boss.txt',
                          header=None, names=['mobileno'])
data_num_ld['tag'] = 1

# 执行剔除操作
Result = pd.merge(data_num_except, data_num_xzhy,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[Result['tag'] != 1, ['mobileno', 'brand']]
data_num_except = Result.copy()

# 【输出预处理后全量文件】
Result.to_csv(r'剔除后全量.txt',
              sep='|', header=None, index=False)
Result.brand.value_counts().sort_values(ascending=False)  # 查看各品牌数量
Result = pd.read_csv(r'C:\Users\Administrator\Desktop\Native十一月份流失用户\十一月份流失用户（剔除完成）.txt',
                     sep='|', header=None, names=['mobileno', 'brand'])

# 【分品牌拆包】
# 品牌预处理（合并如华为公版、华为战略等操作）
Result.loc[Result['brand'].str.contains('华为'), 'new_brand'] = '华为'
Result.loc[Result['brand'] == '小米', 'new_brand'] = '小米'
Result.loc[Result['brand'] == '魅族', 'new_brand'] = '魅族'
Result.loc[
    ((Result['new_brand'] != '华为') & (Result['new_brand'] != '小米') & (Result['brand'] != '魅族')), 'new_brand'] = '其他'
Result = Result.iloc[:, [0, 2]]
Result['new_brand'].value_counts()
# 分品牌拆包
os.chdir(r'C:\Users\Administrator\Desktop\Native十一月份流失用户')
Result.loc[Result['new_brand'] == '华为', ['mobileno']].to_csv('华为.txt',
                                                         header=None, index=False)
Result.loc[Result['new_brand'] == '小米', ['mobileno']].to_csv('小米.txt',
                                                         header=None, index=False)
Result.loc[Result['new_brand'] == '魅族', ['mobileno']].to_csv('魅族.txt',
                                                         header=None, index=False)
Result.loc[Result['new_brand'] == '其他', ['mobileno']].to_csv('其他.txt',
                                                         header=None, index=False)

Result.loc[(~Result['brand'].str.contains('华为')) & (~Result['brand'].str.contains('OPPO'))].to_csv(
    '其他.txt',
    header=None, index=False)
