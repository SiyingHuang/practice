# -*-coding:utf-8-*-

import pandas as pd
import re
from datetime import datetime
import time
import os
import base64
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
# 1、pattern
# 内容为纯文本回复
s = '2019-12-23 08:09:06.006,None,None,None,None,{"bodyText":"5L2g5aW9","contentType":"text/plain","contributionID":"fdsffdsfsfdfd$%$%^$%^^","conversationID":"fSFDSFDR$%#$%$%$%","destinationAddress":"sip:125666660001@botplatform.rcs.chinamobile.com","messageId":"5eae954c-42ca-4181-9ab4-9c0ef2e2ac66","origUser":"tel:+8613752385051","senderAddress":"tel:+8613752385051"}'
# 内容为按钮点击（json格式）
'''
有'messageId'字段
s = '2020-01-02 08:01:16.016,None,None,None,None,{"bodyText":"eyJyZXNwb25zZSI6eyJyZXBseSI6eyJkaXNwbGF5VGV4dCI6IuaIkeeahOi3qOW5tOekvOeJqSIsInBvc3RiYWNrIjp7ImRhdGEiOiIyMDIwIn0sInR5cGUiOiJyZXBseSJ9fX0=","contentType":"application/vnd.gsma.botsuggestion.response.v1.0+json","contributionID":"ebbf4656-0f20-1038-847a-61cf8499237d","conversationID":"ebbf4400-0f20-1038-9908-472dd277606c","destinationAddress":"sip:12520040106@botplatform.rcs.chinamobile.com","messageId":"ebbf0b7e-0f20-1038-bb44-f52655b3107d","senderAddress":"sip:+8615967160345@zj.ims.mnc000.mcc460.3gppnetwork.org"}'
无'messageId'字段
s = '2019-12-21 09:19:44.044,None,None,None,None,{"bodyText":"PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPFNSIHhtbG5zPSJ1cm46Z3NtYTpwYXJhbXM6eG1sOm5zOnJjczpyY3M6c3BhbXJlcG9ydCI+CiAgPENoYXRib3Q+c2lwOjEyNTIwMDQwMTA2QGJvdHBsYXRmb3JtLnJjcy5jaGluYW1vYmlsZS5jb208L0NoYXRib3Q+CiAgPHNwYW0tdHlwZT48L3NwYW0tdHlwZT4KICA8ZnJlZS10ZXh0PuWkqeWkqemqmuaJsDwvZnJlZS10ZXh0Pgo8L1NSPg==","contentType":"application/vnd.gsma.rcsspam-report+xml","contributionID":"e50a52eb-05bd-1038-a34f-6b0fbc8c4ec3","conversationID":"e50a52b3-05bd-1038-8565-174299c32f4a","destinationAddress":"sip:12520040106@botplatform.rcs.chinamobile.com","senderAddress":"sip:+8618890043156@hn.ims.mnc000.mcc460.3gppnetwork.org"}'
'''
# 2、pattern3
s = '{"response":{"reply":{"displayText":"发现精彩","postback":{"data":"发现精彩"},"type":"reply"}}}'

st = time.time()
os.chdir(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data')
pattern = re.compile(
    r'(.{19}).*?bodyText":"(.*?)".*?contentType":"(.*?)".*?destinationAddress":"sip:(\d*).*?(messageId":"(.*?)".*?)?\+86(\d*).*',
    re.DOTALL)
# pattern = re.compile(
#     r'(.{19}).*?bodyText":"(.*?)".*?contentType":"(.*?)".*?destinationAddress":"sip:(\d*).*?messageId":"(.*?)".*?\+86(\d*).*',
#     re.DOTALL)  # 此正则匹配，若日志中无'messageId'时，则无法匹配成功



pattern2 = re.compile(r'displayText":"(.*?)".*', re.DOTALL)

mp_time, main, called, msg_id, type, body = [], [], [], [], [], []
with open(r'up.txt') as f:

    for s in f:
        gp = pattern.search(s)

        if gp:
            # gp.group()
            mp_time.append(gp.group(1))
            main.append(gp.group(7))
            called.append(gp.group(4))
            msg_id.append(gp.group(6))
            type.append(gp.group(3))
            # body.append(gp.group(2))  # 原始内容为base64加密的字符串
            # body.append(json.loads(base64ToStr(gp.group(2)))['response']['reply'])
            body.append(base64ToStr(gp.group(2)))  # base64加密消息内容转为普通字符串

        else:
            mp_time.append(None)
            main.append(None)
            called.append(None)
            msg_id.append(None)
            type.append(None)
            body.append(None)
data_output = pd.DataFrame({'mp_time': mp_time,
                            'main': main,
                            'called': called,
                            'msg_id': msg_id,
                            'type': type,
                            'body': body})
data_output['body'] = data_output.body.map(lambda x: str(x).replace(" ", ""))      # 去除字段内容中的空格符
data_output.loc[data_output.type == "text/plain", 'type'] = 'text'
data_output.loc[data_output.type.str.contains("botsuggestion"), 'type'] = 'bottom'
data_output.loc[data_output.type.str.contains("report\+xml"), 'type'] = 'comp'
data_output.loc[data_output.type == 'application/vnd.gsma.rcs-ft-http+xml', 'type'] = 'other'
data_output.iloc[5635, 5]

# data_output = data_output.loc[((data_output.type == 'bottom') & (
#     data_output.body.str.contains('response'))) | data_output.type != 'bottom']    # 剔除非文本/按钮回复（即语音等）
# data_output.loc[data_output.type == 'bottom', 'bottom_dis'] = data_output.loc[data_output.type == 'bottom', 'body'].map(
#     lambda x: re.search(pattern2, str(x)).group(1))                                # 提取按钮文本内容

print('本次耗时{:.1f}秒'.format(time.time() - st))


data_output.iloc[:, [0, 1, 2, 3, 4, 6]].to_csv(r'C:\Users\Administrator\Desktop\test.txt',
                                               header=None, index=False)
data_output.to_csv(r'C:\Users\Administrator\Desktop\test.txt',
                                               header=None, index=False)

s = '"contentType":"application/vnd.gsma.rcsspam-report+xml"'
s.__contains__()
str(s).contains("gsma")
data_output.loc[data_output.type.notna()]
data_output.loc[data_output.type.isna()]
data_output.loc[[1003,1004, 1005]]
data_output.loc[data_output['type'].str.contains('json')]
