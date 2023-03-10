# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/5/12
# @Author : Owen

import os
import pandas as pd

path = r'D:\中移互联网\财务审计\【3】收集的资料'
os.chdir(path)

xls_list = []

for root, dirs, files in os.walk(path):
    # 遍历文件
    for f in files:
        xls_list.append(os.path.join(root, f))


from pathlib import Path

path = Path(r'D:\中移互联网\财务审计\【3】收集的资料')

for p in path.rglob('*'):
    xls_list.append(p)

with open('test.txt', 'w', encoding='utf-8') as f:
    for i in range(len(xls_list)):
        s = str(xls_list[i]) + '\n'
        f.write(s)
