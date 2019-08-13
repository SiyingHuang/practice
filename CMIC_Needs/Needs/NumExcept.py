import pandas as pd
import numpy as np

# 待剔除号码
data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\一众\魅族_tichu.txt',
                      sep=',', header=None,
                      names=['mobileno'],
                      encoding='GBK')
data_num_except = data_num_except['mobileno'].astype('str')

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
data_num_jituan['mobileno'] = data_num_jituan['mobileno'].astype('str')
data_num_jituan['tag'] = 2

# 执行剔除操作
Result = pd.merge(data_num_except, data_num_jituan,
                  how='left',
                  on='mobileno')
Result = Result.loc[Result['tag'] != 2, ['mobileno']]
Result = pd.DataFrame(Result).drop_duplicates().astype(np.int64)

Result.to_csv(r'C:\Users\Administrator\Desktop\一众\魅族_tichu.txt',
              header=False, index=False)

Result.info()