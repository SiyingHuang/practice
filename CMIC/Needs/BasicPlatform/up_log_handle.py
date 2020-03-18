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
# pattern_body = re.compile(r'"reply":(.*}?).*}}')

mp_time, main, called, msg_id, type, body = [], [], [], [], [], []
with open(r'up.txt') as f:
    for s in f:
        gp = pattern.search(s)
        if gp:
            # gp.group()
            mp_time.append(gp.group(1))
            main.append(gp.group(6))
            called.append(gp.group(4))
            msg_id.append(gp.group(5))
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

data_output['body'] = data_output.body.map(lambda x: str(x).replace(" ", ""))                    # 去除字段内容中的空格符
data_output['type'] = data_output.type.map(lambda x: 'text' if x == 'text/plain' else 'bottom')  # 指定上行消息类型（文字回复or按钮点击）
data_output = data_output.loc[
    (data_output.type == 'bottom') & (data_output.body.str.contains('response'))]  # 剔除非文本/按钮回复（即语音等）

print('本次耗时{:.1f}秒'.format(time.time() - st))


x = '{"response":{"reply":{"displayText":"发现精彩","postback":{"data":"发现精彩"},"type":"reply"}}}'
data_output.loc[data_output.type == 'bottom', 'body'].map(lambda x: json.loads(str(x))['response'])
data_output.loc[data_output.type == 'bottom', 'body'].map(lambda x: json.loads(str(x))['response']['reply'])

data_output.loc[data_output.type == 'bottom', 'body'].to_csv(r'C:\Users\Administrator\Desktop\test.txt',
                                                             header=None, index=False)
