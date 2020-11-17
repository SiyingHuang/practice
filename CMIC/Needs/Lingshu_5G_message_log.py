import numpy as np
import pandas as pd
import re
import time
import os
os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】')


# 测试
log_08 = pd.read_csv(r'F:\HN20201113\UP0820201113010001.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python')
data1 = log_08.loc[(log_08['ua'].map(lambda x: 'UP_2.4' in x)) & (log_08['ua'].map(lambda x: 'Meiz' not in x))]

s = 'CPM-client/OMA2.2 RCS-client/UP_2.4 term-Mi/MI_Mi-10-V12.0.8.0.QJBCNXM client-JUPH/GB-2.0 OS-Android/V12.0.8.0.QJBCNXM;urn%3Aurn-7%3A3gpp-application.ims.iari.rcs.chatbot.sa;"+g.gsma.rcs.botversion=""#=1,#=2""";sip:+8613556425541@gd.5GMC.ims.mnc000.mcc460.3gppnetwork.org'
pattern = re.compile(r'UP_2.4 term-(.*)/(.*) client.*sip:\+86(\d*)@(.*?)\.')
gp = re.search(pattern, s)
gp.groups()


# 分块读取处理


st = time.time()

log_09 = pd.read_csv(r'HN20201113\合并\UP.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python', chunksize=100000)  # 分块读取原始日志
chatbot_data = []
for i in log_09:
    tmp = i.loc[(i['ua'].map(lambda x: 'UP_2.4' in x)) & (i['ua'].map(lambda x: 'Meiz' not in x)) & (
        i['ua'].map(lambda x: 'GB' not in x))]
    chatbot_data.append(tmp)
chatbot_data = pd.concat(chatbot_data, ignore_index=True)

print('耗时{:.4f}秒'.format(time.time() - st))


def extract_brand(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(1)
    else:
        return 'else'


def extract_term(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(2)
    else:
        return 'else'


def extract_mobileno(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(3)
    else:
        return 'else'


def extract_prov(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(4)
    else:
        return 'else'


st = time.time()
result = pd.DataFrame(columns=['brand', 'term', 'mobileno', 'code'])
result['brand'] = chatbot_data['ua'].map(extract_brand)
result['term'] = chatbot_data['ua'].map(extract_term)
result['mobileno'] = chatbot_data['ua'].map(extract_mobileno)
result['code'] = chatbot_data['ua'].map(extract_prov)
print('耗时{:.4f}秒'.format(time.time() - st))


chatbot_data.to_csv(r'HN20201113\符合4个条件原始日志.txt',
                    header=None, index=False)
result.to_csv(r'HN20201113\result.txt',
              index=False)
result = pd.read_csv(r'HN20201113\符合3个条件处理后4个字段.txt', dtype='str')
result = result.drop_duplicates()  # 去重
tmp = result.groupby(by=['code', 'brand', 'term'])['mobileno'].count()  # 去重后统计
tmp = tmp.reset_index(drop=False)

prov_code = pd.read_excel(r'5G消息各大区省份编码.xlsx', names=['code', 'prov'])  # “编码-省份”映射表
tmp2 = pd.merge(tmp, prov_code, on='code')
tmp2.to_excel(r'汇总统计.xlsx', index=False)
