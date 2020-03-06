#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'zhanchengzong' Date: '2019-07-08'
# Example: python C:\Users\CMIC\Desktop\split_mobileno_to_xls_template.py C:\Users\CMIC\Desktop\new_folder

import pandas as pd
import numpy as np
from datetime import datetime
import time
import os
import sys


def split_data_to_excel():
    try:
        PATH = sys.argv[1]                                  # 文件夹名称（文件夹路径，为传入的第2个参数）
    except:
        print(
            '传入参数有误，请重新输入！用法示例：python C:\\Users\\CMIC\\Desktop\\split_mobileno_to_xls_template.py '
            'C:\\Users\\CMIC\\Desktop\\new_folder')
        sys.exit(0)

    if not os.path.exists(PATH):                            # 判断文件夹路径是否不存在
        print('输入的文件路径不存在!请重新输入')
        sys.exit(0)

    st = time.time()                                        # 记录任务开始时间
    print('任务开始!时间:{}'.format(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')))

    NUMS = 1000000                                          # 拆分成每个excel文件的行数
    all_files = os.listdir(PATH)                            # 返回路径下文件名称的列表
    files = []                                              # files为待处理的文件列表
    for file in all_files:                                  # 遍历路径下的所有文件或文件夹
        if os.path.isfile(os.path.join(PATH, file)):        # 把目录PATH和文件名file拼接成一个完整文件路径，再判断该路径是否为文件
                                                            # （如'C:\\Users\\CMIC\\Desktop\\new_folder\\huawei8_result.txt'）
            files.append(file)                              # 若为文件，则将该路径加入files列表中

    if not files:                                           # 检查txt文件是否不存在
        print('文件夹中没有txt数据文件!请检查!')
        return None

    for file in files:  # 遍历每一个文件
        name = file[:-len(file.split('.')[-1]) - 1]       # 防止文件名中有多个.（如示例.示例.txt）；取最后一个.之前的内容作为文件名
        if not os.path.exists(os.path.join(PATH, name)):  # 若文件夹（切分后文件存放的文件夹）不存在，则新建文件夹（名称为'name'）
            os.mkdir(os.path.join(PATH, name))
        else:                                             # 若文件夹存在，则清空里面的内容
            old_files = os.listdir(os.path.join(PATH, name))
            for i in old_files:
                os.remove(os.path.join(PATH, name, i))    # 清空文件夹中的每个文件

        file_path = os.path.join(PATH, file)
        data = pd.read_csv(file_path, skiprows=0, names=['中国移动手机号'], dtype={'中国移动手机号': 'str'})
        if data.shape[0] % NUMS == 0:
            n = data.shape[0] // NUMS
        else:
            n = (data.shape[0] // NUMS) + 1

        print('正在处理文件：{}...'.format(file))
        for i in range(n):
            tmp = data.iloc[i * NUMS: (i + 1) * NUMS].copy()
            tmp['姓名'] = np.nan  # '姓名'列赋'NaN'值
            tmp = tmp[['姓名', '中国移动手机号']]
            tmp['所属分组'] = name
            tmp.to_excel(os.path.join(PATH, name, '{}_{}.xlsx'.format(name, i + 1)), index=False)
            print('第{}组完成!'.format(i + 1))

    print('任务完成!耗时{:.0f}秒!'.format(time.time() - st))
    return None


if __name__ == '__main__':
    split_data_to_excel()
