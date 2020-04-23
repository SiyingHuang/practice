'''
分APP（auser）、分端（user_agent）两个字段：{
    和飞信：'5d36b5b34e3f4601103c819c'
        iOS：'AndFetion'
        Android：'HFX'
    和办公：'5d3fdc22dbdd7a668be5fbff'
        iOS：'AndFetion'
        Android：'okhttp/${project.version}'
}
'''

import pandas as pd
import numpy as np
import os
import time

pd.set_option('display.max_columns', 300)
pd.set_option('display.width', 600)

os.chdir(r'C:\Users\Administrator\Desktop')

# 【匹配后日志】
name_list = ['adate', 'type', 'main_number', 'called_number', 'msg_scene', 'content_type', 'msg_id', 'status_code',
             'msg_type', 'content', 'app_version', 'term_brand', 'termtype_or_iosversion', 'ip', 'p_day_id']
col_type = dict.fromkeys(
    ['type', 'main_number', 'called_number', 'msg_scene', 'content_type', 'msg_id', 'status_code', 'msg_type',
     'content', 'ip', 'p_day_id'], 'str')
path = r'SELF_INNOVATE_ORIGIN_MESSAGE_20200422.txt'
data = pd.read_csv(path,
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   # parse_dates=[0],
                   engine='python', encoding='utf-8')
len(data.loc[data.msg_id.isna()])  # 被叫号码缺失记录

# iPhone、Android日志条数检查
tmp3 = data.loc[data.p_day_id == '20200420'].copy()
tmp3['new_brand'] = tmp3.term_brand.apply(lambda x: 'iPhone' if x == 'iPhone' else 'Android')
tmp3.new_brand.value_counts()

# 统计和飞信APP发送消息成功情况
data.p_day_id.value_counts()
data['new_type'] = data.type.apply(type_distinguish)
# data.drop(columns='new_type', inplace=True)

# st = time.time()
tmp2 = data.loc[
    # (data.p_day_id == '20200419') &  # 日期
    # (data.type == '5d36b5b34e3f4601103c819c') &  # 和飞信
    (data.msg_type == 'postMessage') &  # 发消息
    (data.status_code.map(lambda x: str(x).startswith(('2', '3'))))].copy()  # 成功
# print('耗时{:.4f}秒'.format(time.time() - st))
tmp2.groupby(by=['p_day_id', 'new_type', 'msg_scene'])['msg_id'].nunique()  # 去重统计
tmp2.groupby(by=['p_day_id', 'new_type', 'msg_scene'])['main_number'].nunique()  # 去重统计
tmp2.pivot_table(values=['main_number'],
                 index=['p_day_id', 'new_type'],
                 columns=['msg_scene'],
                 aggfunc=pd.Series.nunique,  # 去重统计
                 margins=True)
tmp2.loc[(tmp2.new_type == 'others')]  # 异常日志检查
tmp2.loc[tmp2.msg_id.duplicated()]
tmp2.loc[tmp2.msg_id == '5e036838848111eaa350005056ad0070']



# 【原始日志】
name_list = ['adate', 'member_function', 'x_real_id', 'http_uri', 'user_agent', 'auser', 'result', 'dtime']
col_type = dict.fromkeys(['member_function', 'x_real_id', 'http_uri', 'user_agent', 'auser', 'result', 'dtime'], 'str')
data = pd.read_csv(r'SELF_INNOVATE_ORIGIN_MESSAGE_TEMP_ALL_CHK.txt',
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   engine='python', encoding='utf-8')  # 0416：1499403条记录
data['type'] = data.auser.map(lambda x: str(x)[:24])  # 区分和飞信、和办公
data['main_number'] = data.auser.map(lambda x: str(x)[-11:])  # 主叫号码
data.dtime.value_counts()

error_list = list(tmp2.loc[tmp2.called_number.isna(), 'adate'])
tmp = data.loc[
    (data.dtime == '20200416') & (data.type == '5d36b5b34e3f4601103c819c') & (data.member_function == 'postMessage') &
    (data.adate.isin(error_list))]
tmp.to_csv(r'test.txt', index=False)


# 区分和飞信、和办公、PC
def type_distinguish(x):
    if x == '5d36b5b34e3f4601103c819c':     # 和飞信
        return 'hfx'
    elif x == '5d3fdc22dbdd7a668be5fbff':   # 和办公
        return 'hbg'
    else:
        return 'others'

# 字典合并
def dict_merge(d1, d2):
    return d1.update(d2)