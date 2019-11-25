# 【核查3】
# 小米限制新增活跃时间的有效结算明细中，剔除号码/IMEI为空的号码量

import pandas as pd
import os

os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\结算明细\限制首月活跃晚于新增')


# 【10月】
data10 = pd.read_csv(r'MI_NEW_201810.txt',
                     sep='|', header=None, encoding='gbk',
                     names=['date', 'mobileno', 'term_type', 'imei', 'sys', 'if_next1', 'if_next2'])
data10 = data10.loc[(data10.if_next1 == '是') & (data10.if_next2 == '是')].iloc[:, [0, 1, 2, 3, 4]]
# 剔除号码或IMEI为空的
data10.loc[data10.mobileno.isna()]  # 0个号码为空
data10.loc[data10.imei.isna()]  # 2个IMEI为空
data10 = data10.loc[(data10.mobileno.notna()) & (data10.imei.notna())]  # 剔除号码或IMEI为空的（470219个）
# 查看号码IMEI重复情况
data10.loc[data10.mobileno.duplicated(), 'mobileno']
data10.loc[data10.imei.duplicated(), 'imei']  # 431个重复IMEI
# 保证号码、IMEI均唯一
data10 = data10.sort_values(by=['date', 'mobileno', 'term_type', 'imei', 'sys'], ascending=True)
data10 = data10.drop_duplicates(subset='imei')
data10 = data10.drop_duplicates(subset='mobileno')


# 【11月】
data11 = pd.read_csv(r'MI_NEW_201811.txt',
                     sep='|', header=None, encoding='gbk',
                     names=['date', 'mobileno', 'term_type', 'imei', 'sys', 'if_next1', 'if_next2'])
data11 = data11.loc[(data11.if_next1 == '是') & (data11.if_next2 == '是')].iloc[:, [0, 1, 2, 3, 4]]
data11.loc[data11.mobileno.isna()]  # 0个号码为空
data11.loc[data11.imei.isna()]  # 5个IMEI为空
data11 = data11.loc[(data11.mobileno.notna()) & (data11.imei.notna())]  # 剔除号码或IMEI为空的（3569661个）
# 查看号码IMEI重复情况
data11.loc[data11.mobileno.duplicated(), 'mobileno']
data11.loc[data11.imei.duplicated(), 'imei']  # 4338个重复IMEI
# 保证号码、IMEI均唯一
data11 = data11.sort_values(by=['date', 'mobileno', 'term_type', 'imei', 'sys'], ascending=True)
data11 = data11.drop_duplicates(subset='imei')
data11 = data11.drop_duplicates(subset='mobileno')

# 【12月】
data12 = pd.read_csv(r'MI_NEW_201812.txt',
                     sep='|', header=None, encoding='gbk',
                     names=['date', 'mobileno', 'term_type', 'imei', 'sys', 'if_next1', 'if_next2'])
data12 = data12.loc[(data12.if_next1 == '是') & (data12.if_next2 == '是')].iloc[:, [0, 1, 2, 3, 4]]
data12.loc[data12.mobileno.isna()]  # 0个号码为空
data12.loc[data12.imei.isna()]  # 5242个IMEI为空
data12 = data12.loc[(data12.mobileno.notna()) & (data12.imei.notna())]  # 剔除号码或IMEI为空的（3445275个）
# 查看号码IMEI重复情况
data12.loc[data12.mobileno.duplicated(), 'mobileno']
data12.loc[data12.imei.duplicated(), 'imei']  # 3988个重复IMEI
# 保证号码、IMEI均唯一
data12 = data12.sort_values(by=['date', 'mobileno', 'term_type', 'imei', 'sys'], ascending=True)
data12 = data12.drop_duplicates(subset='imei')
data12 = data12.drop_duplicates(subset='mobileno')

# 输出结算明细数据
data10.to_csv(r'MI_201810(mobileno&imei_drop_duplicates).txt', sep='|', header=None, index=False)
data11.to_csv(r'MI_201811(mobileno&imei_drop_duplicates).txt', sep='|', header=None, index=False)
data12.to_csv(r'MI_201812(mobileno&imei_drop_duplicates).txt', sep='|', header=None, index=False)
