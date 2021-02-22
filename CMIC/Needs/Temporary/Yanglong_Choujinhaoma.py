# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/22
# @Author : Owen

import numpy as np
import pandas as pd
import os
import time

os.chdir(r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据')
file_list = os.listdir(r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\测试')  # 待处理文件路径
result_path = r'C:\Users\M.Owen\Desktop\附件1：反馈给市场部的明细数据\处理后'  # 结果输出路径

conti_numbers = pd.read_csv(r'C:\Users\M.Owen\Desktop\附件2：连号号码明细out20210113numberinsamewannum-ppcg1301.txt',
                            header=None, names=['mobileno'], dtype=np.int64)
conti_numbers['是否连续号码'] = '是'


print('开始处理..\n')
st = time.time()

for file in file_list:
    st2 = time.time()

    file_name = file[:-5]

    excel_data = pd.read_excel(file)
    result = pd.merge(excel_data, conti_numbers, how='left',
                      left_on='用户标识', right_on='mobileno')
    result.loc[result['是否连续号码'] != '是', '是否连续号码'] = '否'

    result.drop(columns=['mobileno'], inplace=True)

    result.to_excel(os.path.join(result_path, file_name + '（已匹配）.xlsx'), index=False)

    print('完成：{name}'.format(name=file))
    print('耗时{:.4f}秒\n'.format(time.time() - st2))

print('全部处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


"""特殊文件处理"""
file_name = '5-8月数据明细(201805-201808)'
excel_data = pd.read_excel(r'5-8月数据明细(201805-201808).xlsx', sheet_name='明细')
