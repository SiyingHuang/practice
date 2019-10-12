# 小米12月有效结算差异数据核查
# 我方有、厂家无，差异号码量：6447713个
import pandas as pd

cj_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\厂家提供12月有效明细\new_rcs_12月有效结算.txt',
                      header=None, names=['mobileno'])
our_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\jiesuan_xiaomi\MI_NEW_201812.txt',
                       sep='|', header=None, encoding='gbk')
our_data = (our_data.loc[(our_data[5] == '是') & (our_data[6] == '是')][1]).drop_duplicates()
our_data = pd.DataFrame(our_data)
our_data.rename(columns = {1: 'mobileno'}, inplace=True)
our_data['tag'] = 1
Result = pd.merge(cj_data, our_data, how='left', on=['mobileno'])
len(Result.loc[Result['tag'] != 1])  # 644713个号码

# 差异核查过程
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


file_path2 = r'C:\Users\Administrator\Desktop\小米结算差异数据核查\20190816分析报告\jiesuan_new_active_notinour_jiesuan_check_all.txt'
data_jiesuan2 = pd.read_csv(file_path2,
                           sep='|', header=None, encoding='utf-8')
data_jiesuan2.loc[(data_jiesuan2[2].isna()) | (data_jiesuan2[3].isna()) | (data_jiesuan2[4].isna()) | (data_jiesuan2[5].isna())].drop_duplicates(0).iloc[:,0].size
data_jiesuan2.loc[(data_jiesuan2[4] != '小米')].drop_duplicates(0).iloc[:,0].size

# Step1、全量差异号码：644713个
# 任一个月无符合结算条件（不限品牌）号码：139126个
tmp = data_jiesuan2.loc[(data_jiesuan2[2].isna())
                        | (data_jiesuan2[3].isna())
                        | (data_jiesuan2[4].isna())
                        | (data_jiesuan2[5].isna())]
tmp = pd.DataFrame(tmp[0].drop_duplicates())
tmp[1] = 1
# 全量差异号码：644713个
tmp2 = pd.DataFrame(data_jiesuan2[0].drop_duplicates())
# 剔除不符合条件的号码后剩余：505587个
tmp3 = pd.DataFrame((set(tmp2[0]) - set(tmp[0])))
tmp3[1] = 1

# Step2、剩余：505587个
data_jiesuan2_2 =  pd.merge(data_jiesuan2[:],tmp3[0])



data_jiesuan2_2.loc[(data_jiesuan2_2[2] == '小米') # 12月新增
                    & (data_jiesuan2_2[3] == '小米') # 12月活跃
                    & (data_jiesuan2_2[4] == '小米') # 1月活跃
                    & (data_jiesuan2_2[5] != '小米')] # 2月活跃



data_jiesuan2_2.loc[(data_jiesuan2_2[2] == '小米') # 12月新增
                    & (data_jiesuan2_2[3] == '小米') # 12月活跃
                    & (data_jiesuan2_2[4] == '小米') # 1月活跃
                    & (data_jiesuan2_2[5] != '小米') # 2月活跃
                    & (data_jiesuan2_2[6] == '小米') # 3月活跃
                    & (data_jiesuan2_2[7] == '小米') # 4月活跃
                    & (data_jiesuan2_2[8] == '小米') # 5月活跃
                    & (data_jiesuan2_2[9] == '小米') # 6月活跃
                    & (data_jiesuan2_2[10] == '小米')].drop_duplicates(0).iloc[:,0].size #7月活跃
# 任一个月无小米Native活跃号码：500553个
tmp4 = data_jiesuan2_2.loc[(data_jiesuan2_2[2] == '小米') # 12月新增
                    & ((data_jiesuan2_2[3] != '小米') # 12月活跃
                    | (data_jiesuan2_2[4] != '小米') # 1月活跃
                    | (data_jiesuan2_2[5] != '小米'))] # 2月活跃
tmp4 = pd.DataFrame(tmp4[0].drop_duplicates())
tmp4[1] = 1
# 剔除任一个月无小米Native活跃号码后剩余：
tmp5 = pd.DataFrame((set(data_jiesuan2_2[0]) - set(tmp4[0])))

# Step3、剩余5034个
data_jiesuan2_3 = pd.merge(data_jiesuan2_2[:],tmp5[0])
data_jiesuan2_3 = data_jiesuan2_3.iloc[:,:6]
data_jiesuan2_3[4].value_counts(sort=True, ascending=True)
data_jiesuan2_3.to_csv(r'C:\Users\Administrator\Desktop\5034个号码.txt',
                       header=None, index=False)
# 12月无小米新增号码：3626个
tmp5 = data_jiesuan2_3.loc[(data_jiesuan2_3[2] != '小米')]
tmp5 = pd.DataFrame(tmp5[0].drop_duplicates())
tmp5[1] = 1
# 剔除12月非小米Native新增后剩余：
tmp6 = pd.DataFrame((set(data_jiesuan2_3[0]) - set(tmp5[0])))

# Step4、剩余1408个
data_jiesuan2_4 = pd.merge(data_jiesuan2_3[:],tmp6[0])




our_data = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\06 - 【公版结算】\小米\jiesuan_xiaomi\MI_NEW_201810.txt',
                       sep='|', header=None, encoding='gbk')
our_data.loc[:, 1].drop_duplicates()
our_data = (our_data.loc[(our_data[5] == '是') & (our_data[6] == '是')][1]).drop_duplicates()
our_data = pd.DataFrame(our_data)
our_data.rename(columns={1: 'mobileno'}, inplace=True)
len(our_data)