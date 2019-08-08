import pandas as pd

data_num_except = pd.read_csv(r'C:\Users\Administrator\Desktop\各品牌流失用户数据\其他.txt',
                      sep='|', header=None,
                      names=['mobileno'],
                      encoding='GBK')
data_num_mingan = pd.read_csv(r'C:\Users\Administrator\Desktop\敏感号码.txt',
                      sep='|', header=None,
                      names=['mobileno'])
data_num_mingan['tag'] = 1

Result = pd.merge(data_num_except, data_num_mingan,
                  how='left',
                  on='mobileno')
Result = Result.loc[Result['tag'] != 1]

def My_to_csv(data_ys, csv_name):
    data = data_ys[['mobileno']]
    name = csv_name
    data.to_csv(r'C:\Users\Administrator\Desktop\剔除结果\{}_tichu.txt'.format(name),
                header=False, index=False)

My_to_csv(Result, '其他')