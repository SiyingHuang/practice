import pandas as pd

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_new_basic_end0731.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_native_basic = pd.read_csv(r'C:\Users\Administrator\Desktop\native_new_basic_end0731.txt',
                                sep='|', header=None, usecols=[0], names=['mobileno'])

data_new = data_native_basic.drop_duplicates()