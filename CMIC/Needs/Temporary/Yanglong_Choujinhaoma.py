# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/22
# @Author : Owen

"""
需求人：杨龙
用途：
【注】因几个需求先后提出，导致编写多段代码依次进行处理。
1、连续号码标注
    各excel文件中，
    找出其中号码是否存在“不符合结算的连续号码”文件中，
    并新建一列进行标注。
    【注】对个别格式不规范文件，单独进行处理。
2、单个excel文件中重复号码标注
    同一个excel中，出现重复号码（excel中可能有多个sheet）
    找出单个excel文件中的重复号码，
    并新建一列进行标注。
3、excel中部分号码属于异常号段。
    异常号段：'1719615', '1719706', '1719535', '1455663', '1455664', '1718591', '1702462', '1719249', '1719813', '1701868'
    新建一列进行标注。
4、信息匹配。
    连号号码及其连号数文件，需匹配公司名称、活跃时间(首次)信息。
"""

import numpy as np
import pandas as pd
import os
import time


"""初始化"""
result_path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后'  # 结果输出路径

conti_numbers = pd.read_csv(r'C:\Users\M.Owen\Desktop\附件2：连号号码明细out20210113numberinsamewannum-ppcg1301.txt',
                            header=None, names=['mobileno'], dtype=np.int64)  # 连号号码读取
conti_numbers['是否连续号码'] = '是'

section_numbers = pd.read_csv(r'C:\Users\M.Owen\Desktop\号段号码数.txt')  # 特殊号段读取


# """连续号码标注"""
# os.chdir(r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据')
# file_list = os.listdir(r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据')  # 待处理文件路径
# file_list = [x for x in file_list if x[-4:] == 'xlsx']                          # 筛选出.xlsx文件
#
# print('开始处理..\n')
# st = time.time()
#
# for file in file_list:
#     st2 = time.time()
#
#     file_name = file[:-5]
#
#     if file == '5-8月数据明细(201805-201808).xlsx':          # 特殊格式文件处理
#         excel_data = pd.read_excel(file, sheet_name='明细')
#     else:                                                   # 统一格式文件处理
#         excel_data = pd.read_excel(file)
#
#     result = pd.merge(excel_data, conti_numbers, how='left',
#                       left_on='用户标识', right_on='mobileno')
#     result.loc[result['是否连续号码'] != '是', '是否连续号码'] = '否'
#
#     result.drop(columns=['mobileno'], inplace=True)
#
#     result.to_excel(os.path.join(result_path, file_name + '（已匹配）.xlsx'), index=False)
#
#     print('完成：{name}'.format(name=file))
#     print('耗时{:.4f}秒\n'.format(time.time() - st2))
#
# print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


"""连续号码标注（适用于所有excel文件：单sheet、多sheet等）"""
# 单个excel中包含多个sheet
os.chdir(r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\特殊')
file_list = os.listdir()                                # 待处理文件路径
file_list = [x for x in file_list if x[-4:] == 'xlsx']  # 筛选出.xlsx文件

print('开始处理..\n')
st = time.time()

# file_list = ['11月新增201811-01.xlsx', '12月新增201812-01.xlsx']  # 特殊文件处理
for file in file_list:
    print('正在处理：{file_name}'.format(file_name=file))
    st2 = time.time()

    file_name = file[:-5]
    sheet_list = pd.ExcelFile(file).sheet_names

    writer = pd.ExcelWriter(os.path.join(result_path, file_name + '（已匹配）.xlsx'))   # 新建excel文件

    for sheet in sheet_list:
        excel_data = pd.read_excel(file, sheet_name=sheet)
        result = pd.merge(excel_data, conti_numbers, how='left',
                          left_on='用户标识', right_on='mobileno')
        result.loc[result['是否连续号码'] != '是', '是否连续号码'] = '否'

        result.drop(columns=['mobileno'], inplace=True)
        result.to_excel(writer, sheet_name=sheet, index=False)

        print('完成：{name}'.format(name=sheet))

    writer.save()                                           # 单个excel文件中全部sheet写入完成后保存

    print('完成：{name}'.format(name=file))
    print('耗时{:.4f}秒\n'.format(time.time() - st2))

print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


"""单个excel文件中重复号码标注"""
path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后\去重'
os.chdir(path)
file_list = os.listdir(path)  # 待处理文件路径
file_list = [x for x in file_list if x[-4:] == 'xlsx']

print('开始处理..\n')
st = time.time()

for file in file_list:
    print('正在处理：{file_name}'.format(file_name=file))
    st2 = time.time()

    file_name = file[:-5]
    sheet_list = pd.ExcelFile(file).sheet_names

    data = []

    writer = pd.ExcelWriter(os.path.join(result_path, file_name + '（已标注重复）.xlsx'))   # 新建excel文件

    '''合并excel中所有sheet'''
    # 如果单一excel中有多个sheet，先进行合并
    for sheet in sheet_list:
        excel_data = pd.read_excel(file, sheet_name=sheet,
                                   usecols=[3])

        data.append(excel_data)

    data = pd.concat(data, ignore_index=True)
    dup_data = data.loc[data.duplicated()].copy()
    dup_data['是否重复号码'] = '是'

    '''匹配是否重复'''
    for sheet in sheet_list:
        excel_data = pd.read_excel(file, sheet_name=sheet)
        result = pd.merge(excel_data, dup_data, how='left',
                          on='用户标识')
        result.loc[result['是否重复号码'] != '是', '是否重复号码'] = '否'

        result.to_excel(writer, sheet_name=sheet, index=False)

        print('完成：{name}'.format(name=sheet))

    writer.save()
    print('完成：{name}'.format(name=file))
    print('耗时{:.4f}秒\n'.format(time.time() - st2))

print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


"""
判断号码是否在特定号段中
或
匹配该号段号码总数
"""
path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后\是否在特定号段'
os.chdir(path)
file_list = os.listdir(path)  # 待处理文件路径
file_list = [x for x in file_list if x[-4:] == 'xlsx']

print('开始处理..\n')
st = time.time()

for file in file_list:
    print('正在处理：{file_name}'.format(file_name=file))
    st2 = time.time()

    file_name = file[:-5]
    sheet_list = pd.ExcelFile(file).sheet_names

    writer = pd.ExcelWriter(os.path.join(result_path, file_name + '（已标注特定号段）.xlsx'))  # 新建excel文件

    for sheet in sheet_list:
        excel_data = pd.read_excel(file, sheet_name=sheet)

        '''判断号码是否在特定号段中'''
        # excel_data.loc[excel_data['用户标识'].map(
        #     lambda x: str(x)[:7] in ['1719615', '1719706', '1719535', '1455663', '1455664',
        #                              '1718591', '1702462', '1719249', '1719813', '1701868']), '是否特定号段'] = '是'
        # excel_data.loc[excel_data['是否特定号段'] != '是', '是否特定号段'] = '否'

        '''匹配该号段号码总数'''
        excel_data['号段'] = excel_data['用户标识'].map(lambda x: str(x)[:7]).astype(np.int64)
        excel_data = pd.merge(excel_data, section_numbers, how='left', on='号段')
        excel_data.loc[excel_data['号码数'].isna(), '号码数'] = '-'
        excel_data.drop(columns=['号段'], inplace=True)

        excel_data.to_excel(writer, sheet_name=sheet, index=False)

        print('完成：{name}'.format(name=sheet))

    writer.save()
    print('完成：{name}'.format(name=file))
    print('耗时{:.4f}秒\n'.format(time.time() - st2))

print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


"""匹配客户信息、活跃时间(首次)"""
path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后\匹配客户名称活跃时间'
os.chdir(path)
file_list = os.listdir(path)  # 待处理文件路径
file_list = [x for x in file_list if x[-4:] == 'xlsx']

print('开始处理..\n')
st = time.time()

data = []

'''合并所有号码的①公司名称、②首次活跃时间信息'''
for file in file_list:
    print('正在处理：{file_name}'.format(file_name=file))

    sheet_list = pd.ExcelFile(file).sheet_names

    # file = '12月新增201812-01.xlsx'
    for sheet in sheet_list:
        excel_data = pd.read_excel(file, sheet_name=sheet,
                                   usecols=[2, 3, 4], names=['name', 'mobileno', 'first_active_date'])

        data.append(excel_data)

        print('完成：{name}'.format(name=sheet))

    print('完成：{name}\n'.format(name=file))

data = pd.concat(data, ignore_index=True)
print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))

data['mobileno'] = data['mobileno'].astype(np.int64)
data = data.sort_values(by=['mobileno', 'first_active_date'], ascending={'mobileno': True, 'first_active_date': True})
data.reset_index(inplace=True)
data.drop(columns='index', inplace=True)
data.drop_duplicates(subset='mobileno', keep='first', inplace=True)

path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后\匹配客户名称活跃时间\结果'
os.chdir(path)
conti_data = pd.read_excel(r'号码连号数.xlsx')
result = pd.merge(conti_data, data, how='left', left_on='号码', right_on='mobileno')
result.drop(columns='mobileno', inplace=True)
result.to_excel(r'连号号码匹配结果.xlsx',
                index=False)


"""连号数统计"""
os.chdir(r'C:\Users\M.Owen\Desktop')
data = pd.read_csv(r'testdata.txt')
data.sort_values(by='mobileno', ascending=True, inplace=True)
data.reset_index()
list(data)

for num in zip(data.mobileno):
    print(list(num))