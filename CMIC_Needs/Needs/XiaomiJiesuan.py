import pandas as pd

file_path = r'C:\Users\Administrator\Desktop\小米结算差异数据核查\jiesuan_new_active_notinour_jiesuan_check.txt'
with open(file_path,
          encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data_jiesuan = pd.read_csv(file_path,
                           sep='|', header=None, encoding='utf-8')
tmp = data_jiesuan.loc[data_jiesuan[1].isna()].drop_duplicates(0)
tmp_ = pd.DataFrame(tmp[0])


file_path2 = r'C:\Users\Administrator\Desktop\小米结算差异数据核查\jiesuan_new_active_notinour_jiesuan_check_all.txt'
data_jiesuan2 = pd.read_csv(file_path2,
                           sep='|', header=None, encoding='utf-8')
data_jiesuan2.loc[(data_jiesuan2[2].isna()) | (data_jiesuan2[3].isna()) | (data_jiesuan2[4].isna()) | (data_jiesuan2[5].isna())].drop_duplicates(0).iloc[:,0].size
data_jiesuan2.loc[(data_jiesuan2[4] != '小米')].drop_duplicates(0).iloc[:,0].size

# Step1、全量差异号码：644713个
# 任一个月无符合结算条件（不限品牌）号码：139126个
tmp = data_jiesuan2.loc[(data_jiesuan2[2].isna()) | (data_jiesuan2[3].isna()) | (data_jiesuan2[4].isna()) | (data_jiesuan2[5].isna())]
tmp = pd.DataFrame(tmp[0].drop_duplicates())
tmp[1] = 1
# 全量差异号码：644713个
tmp2 = pd.DataFrame(data_jiesuan2[0].drop_duplicates())
# 剔除不符合条件的号码后剩余：505587个
tmp3 = pd.DataFrame((set(tmp2[0]) - set(tmp[0])))
tmp3[1] = 1

# Step2:、剩余：505587个
data_jiesuan2_2 =  pd.merge(data_jiesuan2[:],tmp3[0])
data_jiesuan2_2.loc[(data_jiesuan2_2[2] == '小米') # 12月新增
                    & (data_jiesuan2_2[3] == '小米') # 12月活跃
                    & (data_jiesuan2_2[4] == '小米') # 1月活跃
                    & (data_jiesuan2_2[5] != '小米') #2月活跃
                    & (data_jiesuan2_2[6] == '小米') # 3月活跃
                    & (data_jiesuan2_2[7] == '小米') # 4月活跃
                    & (data_jiesuan2_2[8] == '小米')].drop_duplicates(0).iloc[:,0].size # 5月活跃