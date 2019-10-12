import pandas as pd
import numpy as np
import datetime

with open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs.txt',
                     header=None, usecols=[0], names=['mobileno'])
data = data.drop_duplicates()
data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\native_active_0908.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])
# data2 = data2.drop_duplicates()
data2['tag'] = 1
Result = pd.merge(data, data2, how='left', on='mobileno')
Result = Result.loc[Result['tag'] == 1]
Result['mobileno'].to_csv(
    r'C:\Users\Administrator\Desktop\烦请提取Native全量用户数据与腾讯提供的华为、小米用户数据包匹配（匹配日活）\小米rcs（匹配后）.txt',
    header=None, index=False)



# 获取文件行数
count = 0
f = open(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\魅族\MMDE20190621011\jiesuan_meizu.txt', 'r')
for line in f.readlines():
    count = count + 1
print(count)




file_dict = {'OPPO': 'A', '锤子': 'B', '海信': 'C', '华为2': 'D', '魅族': 'E', '融聚': 'F', '小米': 'G'}
pieces = []
for file_name, group in file_dict.items():
    path = r'C:\Users\Administrator\Desktop\Native适配机型客户 明细\Native适配机型用户明细1\%s.txt' %file_name
    frame = pd.read_csv(path, header=None, names=['mobileno'])
    frame['group'] = group
    pieces.append(frame)
data = pd.concat(pieces, ignore_index=False)

hfx_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\andfetion_register_1011.txt',
                              sep='|', header=None,
                              names=['mobileno'])
hfx_data['tag'] = 1

Result = pd.merge(data, hfx_data, how='left', on='mobileno')
tmp = Result.loc[Result['tag'] != 1]
tmp.loc[tmp['group'] == 'G']['mobileno'].to_csv(r'C:\Users\Administrator\Desktop\Native适配机型客户 明细\Native适配机型用户明细1\G.txt',
                                                header=None, index=False)