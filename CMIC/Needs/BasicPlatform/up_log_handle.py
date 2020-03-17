# -*-coding:utf-8-*-

import pandas as pd
import re
from datetime import datetime
import time
import os
import json


# base64字符串 → 字符串
def base64ToStr(s):
    '''
    将base64字符串转换为字符串
    :param s:
    :return:
    '''
    strDecode = base64.b64decode(bytes(s, encoding="utf8"))
    return str(strDecode, encoding='utf8')


"""日志样例"""
# 内容为纯文本回复
s = '2019-12-23 08:09:06.006,None,None,None,None,{"bodyText":"5L2g5aW9","contentType":"text/plain","contributionID":"fdsffdsfsfdfd$%$%^$%^^","conversationID":"fSFDSFDR$%#$%$%$%","destinationAddress":"sip:125666660001@botplatform.rcs.chinamobile.com","messageId":"5eae954c-42ca-4181-9ab4-9c0ef2e2ac66","origUser":"tel:+8613752385051","senderAddress":"tel:+8613752385051"}'
# 内容为按钮点击（json格式）
s = '2020-01-02 08:01:16.016,None,None,None,None,{"bodyText":"eyJyZXNwb25zZSI6eyJyZXBseSI6eyJkaXNwbGF5VGV4dCI6IuaIkeeahOi3qOW5tOekvOeJqSIsInBvc3RiYWNrIjp7ImRhdGEiOiIyMDIwIn0sInR5cGUiOiJyZXBseSJ9fX0=","contentType":"application/vnd.gsma.botsuggestion.response.v1.0+json","contributionID":"ebbf4656-0f20-1038-847a-61cf8499237d","conversationID":"ebbf4400-0f20-1038-9908-472dd277606c","destinationAddress":"sip:12520040106@botplatform.rcs.chinamobile.com","messageId":"ebbf0b7e-0f20-1038-bb44-f52655b3107d","senderAddress":"sip:+8615967160345@zj.ims.mnc000.mcc460.3gppnetwork.org"}'


st = time.time()
os.chdir(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data')
pattern = re.compile(r'(.{19}).*?bodyText":"(.*?)".*?contentType":"(.*?)".*?destinationAddress":"sip:(\d*).*?messageId":"(.*?)".*?\+86(\d*).*', re.DOTALL)
pattern_body = re.compile(r'"reply":(.*}?).*}}')

mp_time_l, main_l, called_l, msg_id_l, type_l, body_l = [], [], [], [], [], []
with open(r'up.txt') as f:
    for s in f:
        gp = pattern.search(s)
        if gp:
            # gp.group()
            mp_time_l.append(gp.group(1))
            main_l.append(gp.group(6))
            called_l.append(gp.group(4))
            msg_id_l.append(gp.group(5))
            type_l.append(gp.group(3))
            body_l.append(base64ToStr(gp.group(2)))
            # body_l.append(gp.group(2))

            # 字段解析测试
            # a1 = re.search(pattern_body, base64ToStr(gp.group(2))).group(1)
            # json.loads(a1)

        else:
            mp_time_l.append(None)
            main_l.append(None)
            called_l.append(None)
            msg_id_l.append(None)
            type_l.append(None)
            body_l.append(None)
data_output = pd.DataFrame({'mp_time_l': mp_time_l,
                           'main_l': main_l,
                           'called_l': called_l,
                           'msg_id_l': msg_id_l,
                           'type_l': type_l,
                           'body_l': body_l})

data_output['type'] = data_output.type_l.map(lambda x: 'text' if x == 'text/plain' else 'bottom')  # 指定上行消息类型（文字回复or按钮点击）
print('本次耗时{:.1f}秒'.format(time.time() - st))


"""将json格式的body_l字段解析成字典（！！仍有问题！！）"""
x = '{"response":{"reply":{"displayText":"发现精彩","postback":{"data":"发现精彩"},"type":"reply"}}}'
data_output['body_str'] = data_output.loc[data_output.type == 'bottom']['body_l'].map(lambda x: json.loads(re.search(pattern_body, str(x)).group(1)))
