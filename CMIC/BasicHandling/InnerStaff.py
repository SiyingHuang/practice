"""
需求：处理集团内部员工号码文件
"""


import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\Administrator\Desktop\中国移动集团号码及组织树（合并sheet版）.xlsx',
                     header=None, usecols=[0], names=['mobileno'])
data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树.txt',
                     header=None, usecols=[0], names=['mobileno'])
data['mobileno'] = data['mobileno'].astype('str')
data2 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树（剔除疑似异常号码）.txt',
                     header=None, usecols=[0], names=['mobileno'])
data.loc[data['mobileno'].str.contains('\+'), 'mobileno'].to_csv(r'C:\Users\Administrator\Desktop\tmp.txt',
                                                                 header=None, index=False)
# 处理带"?"的号码
data.loc[data['mobileno'].str.contains('\?'), 'mobileno']
data.loc[data['mobileno'].str.contains('\?'), 'mobileno'] = data.loc[data['mobileno'].str.contains('\?'), 'mobileno'].str.replace('\?', '')
# 处理带+86号码
data.loc[data['mobileno'].str.contains('\+86'), 'mobileno']
data.loc[data['mobileno'].str.contains('\+86'), 'mobileno'] = data.loc[data['mobileno'].str.contains('\+86'), 'mobileno'].map(lambda x: str(x)[-11:])
# 删去带"00852-"号码
data.loc[data['mobileno'].str.contains('00852-'), 'mobileno']
data.drop(index=448343, inplace=True)
# 删去带空格的号码
data.loc[data['mobileno'].str.contains(' '), 'mobileno']
448675    52 67657264
448926    0 125 12155
449146    50 12501739
449440    52 67657264
449691    0 125 12155
449911    50 12501739
data.drop(index=[448675,448926,449146,449440,449691,449911], inplace=True)
# 剔除香港（+852）号码
data.loc[data['mobileno'].map(lambda x: str(x)[0:4] == '+852')]
data = data.loc[data['mobileno'].map(lambda x: str(x)[0:4] != '+852')]
# 处理带"+"的号码
data.loc[data['mobileno'].str.contains('\+'), 'mobileno']
data.loc[data['mobileno'].str.contains('\+'), 'mobileno'] = data.loc[data['mobileno'].str.contains('\+'), 'mobileno'].str.replace('\+', '')
# 剔除号码长度不为11位的号码
data.loc[data['mobileno'].map(lambda x: len(str(x)) != 11)]
data = data.loc[data['mobileno'].map(lambda x: len(str(x)) == 11)]
# 剔除首位不为1的号码
data.loc[data['mobileno'].map(lambda x: str(x)[0] != '1')]
data = data.loc[data['mobileno'].map(lambda x: str(x)[0] == '1')]

# 号码格式转换为整型
data['mobileno'] = data['mobileno'].astype(np.int64)

data.to_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\02 - 【提数】\中国移动集团号码及组织树（剔除疑似异常号码）.txt',
            header=None, index=False)