import pandas as pd
import numpy as np
import os
import random
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt',
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)





count = 0
f = open(r'C:\Users\Administrator\Desktop\hxmz_active_period_M_201909\hxmz_active_period_M_meizu_cunliang_201909.txt',
         encoding='utf-8')
for line in f.readlines():
    count = count+1
print(count)
