# 提取周期内流失用户。
# 原始数据字段：号码、品牌。
# 剔除敏感号码、内部号码、不再下发号码。
# 按品牌拆包，仅输出号码字段。

import pandas as pd
import numpy as np
import os

# 【读取原始文件】
# 切换原始文件路径
os.chdir(r'C:\Users\Administrator\Desktop\请协助提取流失用户数据')

ls_data = pd.read_csv(r'剔除后全量.txt',
                      sep='|', header=None, names=['mobileno', 'brand'])
# 【剔除异常号码】
ls_data.loc[ls_data['mobileno'].map(lambda x: len(str(x)) != 11)]
# Result.loc[Result['mobileno'].map(lambda x: len(str(x)) != 11)]
ls_data = ls_data.loc[ls_data['mobileno'].map(lambda x: len(str(x)) == 11)]
Result = Result.loc[Result['mobileno'].map(lambda x: len(str(x)) == 11)]



# 【剔除敏感号码（多类敏感号码）】
# 单独通过NumExcept.py进行处理

# 【输出预处理后全量文件】
Result = Result.iloc[:, :2]
Result.to_csv(r'剔除后全量.txt',
              sep='|', header=None, index=False)
Result.brand.value_counts().sort_values(ascending=False)  # 查看各品牌数量
Result = pd.read_csv(r'剔除后全量.txt',
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
Result.loc[Result['new_brand'] == '华为', ['mobileno']].drop_duplicates().to_csv('华为.txt',
                                                                               header=None, index=False)
Result.loc[Result['new_brand'] == '小米', ['mobileno']].drop_duplicates().to_csv('小米.txt',
                                                                               header=None, index=False)
Result.loc[Result['new_brand'] == '魅族', ['mobileno']].drop_duplicates().to_csv('魅族.txt',
                                                                               header=None, index=False)
Result.loc[Result['new_brand'] == '其他', ['mobileno']].drop_duplicates().to_csv('其他.txt',
                                                                               header=None, index=False)

Result.loc[(~Result['brand'].str.contains('华为')) & (~Result['brand'].str.contains('OPPO'))].drop_duplicates().to_csv(
    '其他.txt',
    header=None, index=False)
