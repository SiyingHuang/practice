'''
分APP（auser）、分端（user_agent）两个字段：{
    {和飞信：'5d36b5b34e3f4601103c819c'
        iOS：'AndFetion'
        Android：'HFX'},
    {和办公：'5d3fdc22dbdd7a668be5fbff'
        iOS：'AndFetion'
        Android：'okhttp/${project.version}'}
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
path = r'SELF_INNOVATE_ORIGIN_MESSAGE.txt'
data = pd.read_csv(path,
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   parse_dates=[0],
                   engine='python', encoding='utf-8')
len(data.loc[data.msg_id.isna()])  # 被叫号码缺失记录

# iPhone、Android日志条数检查（日志已加入PC端，该段代码暂停使用）
# tmp3 = data.loc[data.p_day_id == '20200423'].copy()
# tmp3['new_brand'] = tmp3.term_brand.apply(lambda x: 'iPhone' if x == 'iPhone' else 'Android')
# tmp3.new_brand.value_counts()

# 一对一被叫号码处理
data.loc[data.msg_scene == '1', 'called_handle'] = data.loc[data.msg_scene == '1'].called_number.map(lambda x: str(x)[-11:])
data.loc[data.msg_scene == '2', 'called_handle'] = data.loc[data.msg_scene == '2'].called_number

# 区分APP/PC、和飞信/和办公
data.p_day_id.value_counts()
data['term'] = data.term_brand.apply(terminal_distinguish)  # 区分APP、PC
data['os'] = data.term_brand.apply(os_distinguish)          # 区分iOS、Android、PC
data['type_name'] = data.type.apply(type_distinguish)        # 区分和飞信、和办公
# data.drop(columns='type_name', inplace=True)

# 筛选出所需日志
# st = time.time()
tmp2 = data.loc[
    # (data.p_day_id == '20200419') &  # 日期
    (data.type == '5d36b5b34e3f4601103c819c') &  # 和飞信
    (data.msg_type == 'postMessage') &  # 发消息
    (data.status_code.map(lambda x: str(x).startswith(('2', '3'))))].copy()  # 成功
tmp2.loc[(tmp2.type_name == 'others') & (tmp2.term == 'PC')]['called_number'].drop_duplicates().to_csv(r'test.txt',
                                                                                                   index=False)  # 异常日志提取
# print('耗时{:.4f}秒'.format(time.time() - st))

# 数据统计
tmp2.groupby(by=['p_day_id', 'type_name', 'msg_scene'])['msg_id'].nunique()  # 去重统计
tmp2.groupby(by=['p_day_id', 'type_name', 'msg_scene'])['main_number'].nunique()  # 去重统计
tmp2.pivot_table(values=['main_number'],
                 index=['p_day_id', 'term', 'type_name'],
                 columns=['msg_scene'],
                 aggfunc=pd.Series.nunique,  # 主叫人数统计
                 margins=True)
tmp2.pivot_table(values=['called_handle'],
                 index=['p_day_id', 'term'],
                 columns=['msg_scene'],
                 aggfunc=pd.Series.nunique,  # 被叫人数统计
                 margins=True)
tmp2.pivot_table(values=['msg_id'],
                 index=['p_day_id', 'term'],
                 columns=['msg_scene'],
                 aggfunc=pd.Series.nunique,  # 消息量统计
                 margins=True)
tmp2.loc[(tmp2.type_name == 'others')]  # 异常日志检查



# 【原始日志】
name_list = ['adate', 'member_function', 'x_real_id', 'http_uri', 'user_agent', 'auser', 'result', 'dtime']
col_type = dict.fromkeys(['member_function', 'x_real_id', 'http_uri', 'user_agent', 'auser', 'result', 'dtime'], 'str')
data = pd.read_csv(r'SELF_INNOVATE_ORIGIN_MESSAGE_TEMP_ALL_CHK.txt',
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   engine='python', encoding='utf-8')
data['type'] = data.auser.map(lambda x: str(x)[:24])             # 区分和飞信、和办公
data['main_number'] = data.auser.map(lambda x: str(x)[-11:])     # 提取主叫号码
data.dtime.value_counts()

error_list = list(tmp2.loc[tmp2.called_number.isna(), 'adate'])
tmp = data.loc[
    (data.dtime == '20200416') & (data.type == '5d36b5b34e3f4601103c819c') & (data.member_function == 'postMessage') &
    (data.adate.isin(error_list))]
tmp.to_csv(r'test.txt', index=False)


# 被叫号码处理
def p2p_called_handle(s):


# 区分操作系统（iOS、Android、其他日志）
def os_distinguish(x):
    if x == 'iPhone':       # iPhone
        return 'iOS'
    elif x == 'PC':         # PC
        return 'PC'
    else:                   # Android
        return 'Android'

# 区分APP、PC、其他日志
def terminal_distinguish(x):
    if x == 'PC':       # PC
        return 'PC'
    else:               # APP
        return 'APP'

# 区分和飞信、和办公、其他日志
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
