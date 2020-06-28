import pandas as pd
import numpy as np
import os


# 1、加载号段表
# (1)号段表1 - 分析组整理号段表
path1 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\号段表-1023更新.csv'
data_section_prov = pd.read_csv(path1, header=None,
                                sep=',',
                                encoding='utf-8',
                                usecols=[0, 2, 3, 4], names=['sec', 'prov', 'city', 'operator'], skiprows=1,
                                dtype={'sec': np.int32})
# (2)号段表2 - 集团每日同步号段表
path2 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\DIM_SECTION_NO_DAY_0610.txt'
data_section_prov = pd.read_csv(path2, header=None, names=['prov', 'city', 'sec'], dtype={'sec': np.int32})  # 提取前7位号段（读入11位号码时）

# 2、原始数据读入
data = pd.read_csv(r'C:\Users\Administrator\Desktop\yy_mz_imei_2.txt', header=None,
                   names=['mobileno', 'imei'])
data = data.loc[data.mobileno.notna()]  # 剔除空号码
data = data.loc[data.imei.notna()]  # 剔除空IMEI
data = data.loc[data.mobileno.map(lambda x: len(str(x)) == 14)]  # 剔除非手机号
data['sec'] = data.mobileno.map(lambda x: str(x)[2:9]).astype(np.int32)

# 3、匹配省份地市信息
data_tmp = pd.merge(data, data_section_prov,
                    how='inner',
                    on='sec')
data_tmp = data_tmp.iloc[:, [0, 1, 3]]
data_tmp.mobileno.drop_duplicates()
data_tmp.to_csv(r'C:\Users\Administrator\Desktop\魅族周期内活跃用户IMEI明细.txt', header=None, index=False)
# (1) 本异网条数统计
tmp1 = data_tmp.pivot_table(values='cnts',
                            columns=['operator'],
                            index=['date'],
                            aggfunc=np.sum,
                            margins=True)
tmp1.to_excel(r'C:\Users\Administrator\Desktop\test.xlsx')
# (2) 指定省份数据提取
tmp2 = data_tmp.loc[data_tmp.prov == '']
