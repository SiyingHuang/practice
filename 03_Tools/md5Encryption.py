"""
通过MD5方式加密文件
"""

import pandas as pd
import hashlib

# 【读取csv文件，并逐行进行MD5加密】
data = pd.read_csv(r'C:\Users\Administrator\Desktop\11月Native活跃用户.txt',
                    header=None, names=['mobileno'])
Result = data['mobileno'].map(lambda x: hashlib.md5(str(x).encode(encoding="utf-8")).hexdigest())
Result.to_csv(r'C:\Users\Administrator\Desktop\11月Native活跃用户(MD5).txt',
              index=False)


# 【定义函数进行字符串MD5加密】
def md5Encode(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def md5str(str):
    m = hashlib.md5(str.encode(encoding="utf-8"))
    return m.hexdigest()

def md5(byte):
    return hashlib.md5(byte).hexdigest()
