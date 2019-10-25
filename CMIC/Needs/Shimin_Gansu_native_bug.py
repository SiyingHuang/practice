# 甘肃批开和飞信，只开通了2新
# 正常来说，需要开通3新才能登录Native，然后才能被计算为Native新增用户
# 但出现了bug，2新用户也能登录Native（计算为Native活跃用户），但未被计算为Native新增用户
# 需要统计该问题的影响面，以及如何从报表角度修复此bug。

import pandas as pd
import numpy as np

with open(r'C:\Users\Administrator\Desktop\hsy_tmp_20191017_gansu_native_basic.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\hsy_tmp_20191017_gansu_native_basic.txt',
                   sep='|', header=None,
                   usecols=[0, 1, 3], names=['date', 'mobileno', 'type'])  # type字段：1：新增用户，2：活跃用户
data['month'] = data['date'].map(lambda x: str(x)[:6])
new_data = (data.loc[data['type'] == 1]).drop_duplicates(subset=['month', 'mobileno'])[['month', 'mobileno']]
act_data = (data.loc[data['type'] == 2]).drop_duplicates(subset=['month', 'mobileno'])[['month', 'mobileno']]

# 【逐月统计 新增/活跃 用户数】
new_data.groupby(by='month').count()['mobileno'].sort_index(ascending=True)  # 新增
act_data.groupby(by='month').count()['mobileno'].sort_index(ascending=True)  # 活跃

# 【查看5月新增加的Native活跃用户情况】
new5 = new_data.loc[new_data['month'] == '201905'][['mobileno']]  # 5月Native新增用户
new5andbefore = (new_data.loc[new_data['month'] <= '201905'][['mobileno']]).drop_duplicates()  # 5月及之前新增用户
new4andbefore = (new_data.loc[new_data['month'] <= '201904'][['mobileno']]).drop_duplicates()  # 4月及之前新增用户
act5 = act_data.loc[act_data['month'] == '201905'][['mobileno']]  # 5月Native活跃用户
act4andbefore = (act_data.loc[act_data['month'] <= '201904'][['mobileno']]).drop_duplicates()  # 4月及之前活跃用户
act5new = pd.DataFrame(set(act5['mobileno'])-set(act4andbefore['mobileno']), columns=['mobileno'])  # 5月当月新增加的活跃用户：41654
len(pd.merge(act5new, new5, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月的Native新增情况：仅有14947个当月有新增记录，其余无。
len(pd.merge(act5new, new5andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月及以前的Native新增情况：仅有16489个有新增记录，其余无。
len(pd.merge(act5new, new4andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在上个月及以前的Native新增情况：仅有1544个有新增记录，其余无。

# 【查看6月新增加的Native活跃用户情况】
new6 = new_data.loc[new_data['month'] == '201906'][['mobileno']]  # 6月Native新增用户
new6andbefore = (new_data.loc[new_data['month'] <= '201906'][['mobileno']]).drop_duplicates()  # 6月及之前新增用户
new5andbefore = (new_data.loc[new_data['month'] <= '201905'][['mobileno']]).drop_duplicates()  # 5月及之前新增用户
act6 = act_data.loc[act_data['month'] == '201906'][['mobileno']]  # 6月Native活跃用户
act5andbefore = (act_data.loc[act_data['month'] <= '201905'][['mobileno']]).drop_duplicates()  # 5月及之前活跃用户
act6new = pd.DataFrame(set(act6['mobileno'])-set(act5andbefore['mobileno']), columns=['mobileno'])  # 6月当月新增加的活跃用户：45293
len(pd.merge(act6new, new6, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月的Native新增情况：仅有360个当月有新增记录，其余无。
len(pd.merge(act6new, new6andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月及以前的Native新增情况：仅有2706个有新增记录，其余无。
len(pd.merge(act6new, new5andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在上个月及以前的Native新增情况：仅有2346个有新增记录，其余无。

# 【查看7月新增加的Native活跃用户情况】
new7 = new_data.loc[new_data['month'] == '201907'][['mobileno']]  # 7月Native新增用户
new7andbefore = (new_data.loc[new_data['month'] <= '201907'][['mobileno']]).drop_duplicates()  # 7月及之前新增用户
new6andbefore = (new_data.loc[new_data['month'] <= '201906'][['mobileno']]).drop_duplicates()  # 6月及之前新增用户
act7 = act_data.loc[act_data['month'] == '201907'][['mobileno']]  # 7月Native活跃用户
act6andbefore = (act_data.loc[act_data['month'] <= '201906'][['mobileno']]).drop_duplicates()  # 6月及之前活跃用户
act7new = pd.DataFrame(set(act7['mobileno'])-set(act6andbefore['mobileno']), columns=['mobileno'])  # 7月当月新增加的活跃用户：70354
len(pd.merge(act7new, new7, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月的Native新增情况：仅有537个当月有新增记录，其余无。
len(pd.merge(act7new, new7andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月及以前的Native新增情况：仅有26962个有新增记录，其余无。
len(pd.merge(act7new, new6andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在上个月及以前的Native新增情况：仅有26425个有新增记录，其余无。

# 【查看8月新增加的Native活跃用户情况】
new8 = new_data.loc[new_data['month'] == '201908'][['mobileno']]  # 8月Native新增用户
new8andbefore = (new_data.loc[new_data['month'] <= '201908'][['mobileno']]).drop_duplicates()  # 8月及之前新增用户
new7andbefore = (new_data.loc[new_data['month'] <= '201907'][['mobileno']]).drop_duplicates()  # 7月及之前新增用户
act8 = act_data.loc[act_data['month'] == '201908'][['mobileno']]  # 8月Native活跃用户
act7andbefore = (act_data.loc[act_data['month'] <= '201907'][['mobileno']]).drop_duplicates()  # 7月及之前活跃用户
act8new = pd.DataFrame(set(act8['mobileno'])-set(act7andbefore['mobileno']), columns=['mobileno'])  # 8月当月新增加的活跃用户：56070
len(pd.merge(act8new, new8, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月的Native新增情况：仅有146个当月有新增记录，其余无。
len(pd.merge(act8new, new8andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月及以前的Native新增情况：仅有7285个有新增记录，其余无。
len(pd.merge(act8new, new7andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在上个月及以前的Native新增情况：仅有7154个有新增记录，其余无。

# 【查看9月新增加的Native活跃用户情况】
new9 = new_data.loc[new_data['month'] == '201909'][['mobileno']]  # 9月Native新增用户
new9andbefore = (new_data.loc[new_data['month'] <= '201909'][['mobileno']]).drop_duplicates()  # 9月及之前新增用户
new8andbefore = (new_data.loc[new_data['month'] <= '201908'][['mobileno']]).drop_duplicates()  # 8月及之前新增用户
act9 = act_data.loc[act_data['month'] == '201909'][['mobileno']]  # 9月Native活跃用户
act8andbefore = (act_data.loc[act_data['month'] <= '201908'][['mobileno']]).drop_duplicates()  # 8月及之前活跃用户
act9new = pd.DataFrame(set(act9['mobileno'])-set(act8andbefore['mobileno']), columns=['mobileno'])  # 9月当月新增加的活跃用户：45852
len(pd.merge(act9new, new9, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月的Native新增情况：仅有53个当月有新增记录，其余无。
len(pd.merge(act9new, new9andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在当月及以前的Native新增情况：仅有2553个有新增记录，其余无。
len(pd.merge(act9new, new8andbefore, how='inner', on='mobileno'))  # 看新增加的活跃用户在上个月及以前的Native新增情况：仅有2503个有新增记录，其余无。
