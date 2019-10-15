# 需求描述：
# 重庆市存量用户月度流失情况

import pandas as pd
import numpy as np

# 【存量用户数据读取】
data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\native_active_201908_and_before.txt',
                    sep='|', header=None, usecols=[0], names=['mobileno'])
data['mobileno'] = data['mobileno'].astype('str')
data['sec'] = data['mobileno'].map(lambda x: str(x)[:7]).astype(np.int32)


# 【筛选出某省份存量用户】
# 号段表读取
path3 = r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\基础数据\DIM_SECTION_NO_DAY_1007.txt'  # 号段表
data_section = pd.read_csv(path3, header=None,
                           sep='|',
                           encoding='utf-8',
                           names=['prov', 'city', 'section_no'])
data_section = data_section.loc[data_section['section_no'].notna()]  # 去除空值（存在省份为其他、中国，而section_no为空的情况）
data_section['section_no'] = data_section['section_no'].astype(np.int32)
# 筛选出重庆存量用户
data_section_prov = data_section.loc[data_section.prov == '重庆']
data = pd.merge(data, data_section_prov,
                how='inner',
                left_on='sec', right_on='section_no')


# 【月活数据读取】
act_data = pd.read_csv(r'C:\Users\Administrator\Desktop\DATA_FUSI_ACTIVE_USER_M_0_4_201909.txt', sep='|', header=None, skiprows=1, usecols=[5], names=['mobileno'])
act_data['mobileno'] = act_data['mobileno'].astype('str')
act_data['tag'] = 1


# 【月度流失用户匹配】
data_tmp = pd.merge(data, act_data,
                    how='left',
                    on='mobileno')
data_tmp = data_tmp.loc[data_tmp['tag'] != 1]['mobileno']
data_tmp['mobileno'].to_csv(r'C:\Users\Administrator\Desktop\重庆移动新业务室数据提取需求\需求2：leiji_active_201909noactive.txt',
                            header=None, index=False)