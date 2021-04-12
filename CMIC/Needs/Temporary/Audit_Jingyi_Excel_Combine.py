# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/2
# @Author : Owen

"""
需求人：杨静宜
需求：财务收支类审计，合并多个excel文件，并保留指定字段。
"""

import pandas as pd
import os
import time

path = r'C:\Users\Administrator\Desktop\【财务收支类问题专项评估】资料需求清单-财务部（补充资料）'
os.chdir(path)
result_path = r'C:\Users\Administrator\Desktop\【财务收支类问题专项评估】资料需求清单-财务部（补充资料）'

file_list = os.listdir(path)  # 待处理文件路径
file_list = [x for x in file_list if x[-4:] == 'xlsx']
sheet_list = '2019年-2020年5月'
sheet_list = '2019年1月-2020年5月团组报账单'
sheet_list = '2020年6月-2021年2月'
sheet_dict = {'2019年-2020年5月': ['部门', '报账单编号', '出差开始日期', '出差返回日期', '出差人', '出发地点', '到达地点', '摘要'],
              '2019年1月-2020年5月团组报账单': ['申请单编号', '出差开始日期', '出差返回日期', '出发地点', '到达地点', '事由及说明', '出差人姓名', '报账人'],
              '2020年6月-2021年2月': ['申请单编号', '出差开始日期', '出差返回日期', '出差人数', '出发地点', '到达地点', '事由及说明', '报账人', '供应商名称', '经办人']}

print('开始处理..\n')
st = time.time()

for sheet in sheet_list:
    print('正在处理：{sheet_name}'.format(sheet_name=sheet))

    data = []
    excel_data = []

    for file in file_list:

        this_sheet_list = pd.ExcelFile(file).sheet_names

        print('正在处理：{file_name}'.format(file_name=file))
        if sheet in this_sheet_list:
            excel_data = pd.read_excel(file, sheet_name=sheet)

            excel_data = excel_data[sheet_dict[sheet_list]]

        data.append(excel_data)

    data = pd.concat(data, ignore_index=True)

    print('正在输出...')
    data.to_excel(os.path.join(result_path, sheet + '.xlsx'), index=False)

    print('完成：{sheet_name}\n'.format(sheet_name=sheet))

print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))
