#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'zhanchengzong' Date: '2019-10-22'
# Example: python C:\Users\CMIC\Desktop\check_for_blacklist.py
# C:\Users\CMIC\Desktop\data.txt header=None usecols=[1] sep='^|'

import pandas as pd
import numpy as np
import time
import os
import sys


def check_for_blacklist():
    print('任务开始！正在处理中...')
    st = time.time()                                                # 记录任务开始时间
    if os.path.basename(FILE).split('.')[-1] in ('xls', 'xlsx'):    # 判断是否为excel格式的文件
        if HEADER == 'infer':  # 未传入header参数（HEADER默认值为'infer'）
            data = pd.read_excel(FILE, header=0, usecols=USECOLS, names=['mobileno'], dtype={'mobileno': np.int64})
        else:                  # 传入header参数
            data = pd.read_excel(FILE, header=HEADER, usecols=USECOLS, names=['mobileno'], dtype={'mobileno': np.int64})
    else:															# 文件非excel格式时
        if HEADER == 'infer':  # 未传入header参数
            data = pd.read_csv(FILE, sep=SEP, header='infer', usecols=USECOLS, names=['mobileno'],
                               dtype={'mobileno': np.int64}, skiprows=1)
        else:                  # 传入header参数
            data = pd.read_csv(FILE, sep=SEP, header=HEADER, usecols=USECOLS, names=['mobileno'],
                               dtype={'mobileno': np.int64})

    black_list = pd.read_excel(r'和飞信免打扰黑名单库.xlsx', usecols=[1])  			# 加载黑名单
    interior = pd.read_csv(r'集团内部号码(2月已处理).csv')  							# 加载集团内部号码
    special = pd.read_csv(r'今年不再发短信的120w号码.csv')  							# 今年不再下发短信的120W号码
    delete = pd.concat([black_list, interior, special], axis=0, ignore_index=True)  # 合并所有需剔除的号码（按行合并，忽略原有索引）

    intersect_num = len(set(data.mobileno) & set(delete.mobileno))					# 查看数据与需剔除的号码是否有交集
    if intersect_num == 0:
        print('验证成功！本次号码与黑名单、集团名单、120W名单无交集！')
    else:
        print('验证失败！数据集号码与黑名单、集团名单、120W名单交集的个数为：{}！请重新处理数据！！！'.format(intersect_num))
    print('本次特殊名单验证耗时{:.1f}秒'.format(time.time() - st))                    # 计算所花费时长
    sys.exit(0)                                                                      # 无错误退出


if __name__ == '__main__':															# Python模拟的程序入口
    # sys.argv：表示命令行参数列表；len(sys.argv)：表示命令行参数个数。
    if len(sys.argv) == 1 or len(sys.argv) > 5:										# 判断传入参数的个数（“python”后为传入参数），至少为2个或不超过5个
        print(r"参数有误，请重新输入！用法示例：python C:\Users\CMIC\Desktop\check_for_blacklist.py "
              r"C:\Users\CMIC\Desktop\data.txt header=None usecols=[1] sep='^|'")
        sys.exit(0)

    FILE = sys.argv[1]																# 向FILE传入第2个参数agrv[1]，为待判断数据的文件名称
    for i in range(2, len(sys.argv)):												# 依次传入第3个及其之后（第3-len(sys.argv)个）的参数
        """将传入的字符串参数，依次执行（如参数3：'header=None'，将执行该语句）"""
        exec(sys.argv[i])

    # dir()：获取当前模块的属性列表
    HEADER = header if 'header' in dir() else 'infer'				# 默认自动推断表头（如果传入header参数，则赋给HEADER；否则默认为'infer'）
    USECOLS = usecols if 'usecols' in dir() else [0]				# 默认首列（第0行）为号码（如果传入usecols参数，则赋给USECOLS；否则默认为'0'）
    SEP = sep if 'sep' in dir() else ','							# 默认分隔符为“,”（如果传入sep参数，则赋给SEP；否则默认为','）

    os.chdir(r'C:\Users\Administrator\Desktop\blacklist')		# 切换到待剔除号码包的文件夹路径下（chdir：change directory）
    check_for_blacklist()										# 执行判别函数

data = pd.read_excel(r'C:\Users\CMIC\Desktop\test\mulcols.xlsx', usecols=[1], names=['mobileno'],
                     dtype={'mobileno': np.int64}, header=0)    # 测试
