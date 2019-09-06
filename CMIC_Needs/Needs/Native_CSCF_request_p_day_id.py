# 入库时间与请求时间差异问题分析
with open(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_qiyuan_cscf_diffierent_time_Aug.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
# 读取原始13202日志
data = pd.read_csv(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_qiyuan_cscf_diffierent_time_Aug.txt',
                   sep='|', header=None, skiprows=0, usecols=[6, 7, 17], names=['mobileno', 'request', 'p_day_id'])
data_ = data.copy()
data['request'] = (data['request'].map(lambda x: str(x)[:8])).astype(np.int64)
data['p_day_id'] = (data['p_day_id'].map(lambda x: str(x)[:8])).astype(np.int64)
data = data.drop_duplicates()
data1 = data[data['p_day_id'] == 20190803]
data1.mobileno.drop_duplicates()
data2 = data[data['p_day_id'] == 20190826]
data2.drop_duplicates()
data_chk = data1.append(data2)
data.to_csv(r'C:\Users\Administrator\Desktop\cscf_different_July.txt',
            sep='|', header=None, index=False)
# 0803: 2594418  0826: 2834026
# 请求早于入库：66/95  请求晚于入库：2594352/2833931
# 0703: 2427223  0726: 2543646
# 请求早于入库：68/102  请求晚于入库：2427155/2543544
# 0603: 2192155  0626: 2358310
# 请求早于入库：81/69  请求晚于入库：2192074/2358241

len(data1[data1['request'] < data1['p_day_id']])
len(data1[data1['request'] > data1['p_day_id']])
len(data2[data2['request'] < data2['p_day_id']])
len(data2[data2['request'] > data2['p_day_id']])

# 读取简化日志
data = pd.read_csv(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_qiyuan_cscf_diffierent_time_Aug_0731to0806.txt',
                   sep='|', header=None, skiprows=0, names=['mobileno', 'request', 'p_day_id'])
data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\tmp_hsy_20190905002_qiyuan_cscf_diffierent_time_Aug_0807to0810.txt',
                   sep='|', header=None, skiprows=0, names=['mobileno', 'request', 'p_day_id'])
data = data.append(data1)
data['request'] = (data['request'].map(lambda x: str(x)[:8])).astype(np.int32)
data['p_day_id'] = (data['p_day_id'].map(lambda x: str(x)[:8])).astype(np.int32)
data = data.drop_duplicates()
tmp = data.groupby(by=['p_day_id', 'request'])['mobileno'].count().unstack()
tmp.to_excel(r'C:\Users\Administrator\Desktop\result.xlsx')