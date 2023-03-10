# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/12
# @Author : Owen

import os
import sys


def file():
    xls_list = []

    for root, dirs, files in os.walk(PATH):
        # 遍历文件
        for f in files:
            xls_list.append(os.path.join(root, f))

    with open(r'file_detail.txt', 'w', encoding='utf-8') as f:
        for i in xls_list:
            s = str(i) + '\n'
            f.write(s)


if __name__ == '__main__':
    PATH = sys.argv[1]
    os.chdir(PATH)
    file()
