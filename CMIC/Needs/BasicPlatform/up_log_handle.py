# -*-coding:utf-8-*-

import pandas as pd
import re
import time
import os
import base64


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
# 2、pattern2
s = '{"response":{"reply":{"displayText":"发现精彩","postback":{"data":"发现精彩"},"type":"reply"}}}'

st = time.time()
os.chdir(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data')
os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【Native】\01 - 【分析】\终端室需求\02.26 信息卡片与文案测试\消息中台')


"""对日志内容进行解析"""
pattern = re.compile(
    r'(.{19}).*?bodyText":"(.*?)".*?contentType":"(.*?)".*?destinationAddress":"sip:(\d*).*?(messageId":"(.*?)".*?)?\+86(\d*).*',
    re.DOTALL)                                                            # 部分日志无"messageId"字段内容
# pattern = re.compile(
#     r'(.{19}).*?bodyText":"(.*?)".*?contentType":"(.*?)".*?destinationAddress":"sip:(\d*).*?messageId":"(.*?)".*?\+86(\d*).*',
#     re.DOTALL)  # 此正则匹配，若日志中无'messageId'时，则无法匹配成功
"""对“建议回复”中的消息内容进行解析"""
pattern2 = re.compile(r'displayText":"(.*?)"(,"postback)?.*', re.DOTALL)  # 部分“建议回复”日志无"postback"字段内容

mp_time, main, called, msg_id, type, body = [], [], [], [], [], []
with open(r'上行.txt') as f:

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

data_output['body'] = data_output.body.map(lambda x: str(x).replace(" ", ""))                   # 去除字段内容中的空格符
data_output['body'] = data_output.body.map(lambda x: str(x).replace("\\\"", "\'"))              # 将字段内容中的“\"”替换为“'”（如“共同战“疫””）
data_output.loc[data_output.type == "text/plain", 'type'] = 'text'                              # 文字输入回复
data_output.loc[data_output.type.str.contains("botsuggestion"), 'type'] = 'bottom'              # 建议回复（按钮）
data_output.loc[data_output.type.str.contains("report\+xml"), 'type'] = 'comp'                  # 投诉
data_output.loc[data_output.type.str.contains("botsharedclientdata"), 'type'] = 'tsr'           # 终端状态上报
data_output.loc[data_output.type == 'application/vnd.gsma.rcs-ft-http+xml', 'type'] = 'others'  # 其它消息体（用户上行语音、文件等）

data_output.loc[data_output.type == 'bottom', 'bottom_dis'] = data_output.loc[data_output.type == 'bottom', 'body'].map(
    lambda x: re.search(pattern2, str(x)).group(1) if re.search(pattern2, str(x)) else str(x))  # 提取按钮文本内容

print('本次耗时{:.1f}秒'.format(time.time() - st))


data_output.loc[data_output.type=='bottom', 'body'].to_csv(r'C:\Users\Administrator\Desktop\test.txt', header=None, index=False)
data_output.loc[data_output.type=='bottom', 'bottom_dis'].to_csv(r'C:\Users\Administrator\Desktop\test2.txt', header=None, index=False)

data_output.columns
data_output.iloc[:, [0, 1, 2, 3, 4, 6]].to_csv(r'C:\Users\Administrator\Desktop\test.txt', header=None, index=False)


top_bottom = data_output.loc[data_output.type == 'bottom'].groupby(by='called')['called'].count().sort_values(ascending=False).index
top10_data = data_output.loc[data_output.called.isin(top_bottom[:10])]
top10_result = top10_data.groupby(by=['called', 'bottom_dis'])['mp_time'].count().to_frame()
top10_result.reset_index(inplace=True)
top10_result.columns = ['called', 'bottom_dis', 'counts']
top10_result.to_csv(r'C:\Users\Administrator\Desktop\test.txt', index=False)
