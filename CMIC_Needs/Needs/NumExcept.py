# 对原始数据，剔除指定号码

import pandas as pd
import numpy as np

# 待剔除号码
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\native_liushi_JulynotAug.txt',
                      sep='|', header=None,
                      names=['mobileno', 'brand'])
data_num_except = pd.read_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1.xlsx',
                                header=None,
                                names=['mobileno'],
                                encoding='GBK')
data_num_except['mobileno'] = data_num_except['mobileno'].astype('str')

# 需剔除号码1
data_num_mingan = pd.read_csv(r'C:\Users\Administrator\Desktop\敏感号码.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num_mingan['mobileno'] = data_num_mingan['mobileno'].astype('str')
data_num_mingan['tag'] = 1

# 需剔除号码2
data_num_jituan = pd.read_csv(r'C:\Users\Administrator\Desktop\中国移动集团号码及组织树.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num_jituan = data_num_jituan['mobileno'].map(lambda x: str(x)[-11:])
data_num_jituan = pd.DataFrame(data_num_jituan)
# 集团号码txt文件中，存在带+86的号码
data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 2

# 执行剔除操作
Result = pd.merge(data_num_except, data_num_mingan,
                  how='left',
                  on='mobileno')
Result.loc[Result['tag'] == 1]
Result = Result.loc[Result['tag'] != 1]
Result['mobileno'] = Result['mobileno'].astype(np.int64)
Result = pd.DataFrame(Result).drop_duplicates().astype(np.int64)

Result.iloc[:, :2].to_csv(r'C:\Users\Administrator\Desktop\native_liushi_JulynotAug（剔除后）.txt',
                          sep='|', header=False, index=False)
Result.to_excel(r'C:\Users\Administrator\Desktop\200W未开通号码_1（剔除后）.xlsx',
                header=False, index=False)

Result.iloc[:, :3].to_csv(r'C:\Users\Administrator\Desktop\请协助提取native活动第二批数据，谢谢\结果\result_all_tichu.txt',
              sep='|', header=False, index=False)