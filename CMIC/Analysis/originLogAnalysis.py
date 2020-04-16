'''
分APP（auser）、分端（user_agent）
    和飞信：5d36b5b34e3f4601103c819c
        iOS：AndFetion
        Android：HFX
    和办公：5d3fdc22dbdd7a668be5fbff
        iOS：AndFetion
        Android：okhttp/${project.version}
'''


import pandas as pd
import numpy as np
import os


def dict_merge(d1, d2):
    return d1.update(d2)


os.chdir(r'C:\Users\Administrator\Desktop')
name_list = ['adate', 'type', 'main_number', 'called_number', 'msg_scene', 'content_type', 'msg_id', 'status_code',
             'msg_type', 'content', 'app_version', 'term_brand', 'termtype_or_iosversion', 'ip', 'p_day_id']
col_type = dict.fromkeys(['type', 'main_number', 'called_number', 'status_code', 'p_day_id'], 'str')
data = pd.read_csv(r'SELF_INNOVATE_ORIGIN_MESSAGE_TEMP_ALL.txt',
                   sep=r'@@sep',
                   names=name_list, dtype=col_type,
                   parse_dates=[0], engine='python', encoding='utf-8')
data.p_day_id.value_counts()
tmp = data.loc[(data.type == '5d3fdc22dbdd7a668be5fbff') & (data.msg_type == 'postMessage')]

