'''
分APP（auser）、分端（user_agent）两个字段：{
    和飞信：5d36b5b34e3f4601103c819c
        iOS：AndFetion
        Android：HFX
    和办公：5d3fdc22dbdd7a668be5fbff
        iOS：AndFetion
        Android：okhttp/${project.version}
}
'''

import pandas as pd
import numpy as np
import os


def dict_merge(d1, d2):
    return d1.update(d2)


os.chdir(r'C:\Users\Administrator\Desktop')

# 【匹配后日志】
name_list = ['adate', 'type', 'main_number', 'called_number', 'msg_scene', 'content_type', 'msg_id', 'status_code',
             'msg_type', 'content', 'app_version', 'term_brand', 'termtype_or_iosversion', 'ip', 'p_day_id']
col_type = dict.fromkeys(['type', 'main_number', 'called_number', 'msg_scene', 'status_code', 'p_day_id'], 'str')
data = pd.read_csv(r'SELF_INNOVATE_ORIGIN_MESSAGE_TEMP_ALL.txt',
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   # parse_dates=[0],
                   engine='python', encoding='utf-8')
len(data.loc[data.called_number.isna()])  # 被叫号码缺失记录

# iPhone、Android日志条数检查
tmp3 = data.loc[data.p_day_id == '20200416']
tmp3['new_brand'] = tmp3.term_brand.apply(lambda x: 'iPhone' if x == 'iPhone' else 'Android')
tmp3.new_brand.value_counts()

# 统计和飞信APP消息成功情况
data.p_day_id.value_counts()
tmp2 = data.loc[
    (data.p_day_id == '20200416') &  # 日期
    (data.type == '5d36b5b34e3f4601103c819c') &  # 和飞信
    (data.msg_type == 'postMessage') &
    ((data.status_code.map(lambda x: '2' in str(x)[0])) | (data.status_code.map(lambda x: '3' in str(x)[0])))]  # 成功
len(tmp2.main_number.drop_duplicates())  # 主叫人数统计
len(tmp2.msg_id.drop_duplicates())  # 消息条数统计
tmp2.term_brand.value_counts()
tmp2.groupby(by=['p_day_id'])['main_number'].count()
len(tmp2.loc[tmp2.called_number.isna()])




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
