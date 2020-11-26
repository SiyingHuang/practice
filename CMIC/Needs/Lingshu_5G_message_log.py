import numpy as np
import pandas as pd
import re
import time
import os
os.chdir(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】\HN20201126')


# 测试
log_08 = pd.read_csv(r'F:\HN20201113\UP0820201113010001.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python')
data1 = log_08.loc[(log_08['ua'].map(lambda x: 'UP_2.4' in x)) & (log_08['ua'].map(lambda x: 'Meiz' not in x))]

s = 'CPM-client/OMA2.2 RCS-client/UP_2.4 term-Mi/MI_Mi-10-V12.0.8.0.QJBCNXM client-JUPH/GB-2.0 OS-Android/V12.0.8.0.QJBCNXM;urn%3Aurn-7%3A3gpp-application.ims.iari.rcs.chatbot.sa;"+g.gsma.rcs.botversion=""#=1,#=2""";sip:+8613556425541@gd.5GMC.ims.mnc000.mcc460.3gppnetwork.org'
pattern = re.compile(r'UP_2.4 term-(.*)/(.*) client.*sip:\+86(\d*)@(.*?)\.')
gp = re.search(pattern, s)
gp.groups()


# 1、分块读取处理：筛选出符合条件日志
st = time.time()

log_up = pd.read_csv(r'UP.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python', chunksize=100000)  # 分块读取原始日志
chatbot_data = []
for i in log_up:
    tmp = i.loc[(i['ua'].map(lambda x: 'UP_2.4' in x)) & (i['ua'].map(lambda x: 'Meiz' not in x)) & (
        i['ua'].map(lambda x: 'GB' not in x))]
    chatbot_data.append(tmp)
chatbot_data = pd.concat(chatbot_data, ignore_index=True)

print('耗时{:.4f}秒'.format(time.time() - st))


pattern = re.compile(r'UP_2.4 term-(.*)/(.*) client.*sip:\+86(\d*)@(.*?)\.')

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


# 2、提取所需信息：品牌、机型、号码、省份
st = time.time()
result = pd.DataFrame(columns=['brand', 'term', 'mobileno', 'code'])
result['brand'] = chatbot_data['ua'].map(extract_brand)
result['term'] = chatbot_data['ua'].map(extract_term)
result['mobileno'] = chatbot_data['ua'].map(extract_mobileno)
result['code'] = chatbot_data['ua'].map(extract_prov)
print('耗时{:.4f}秒'.format(time.time() - st))


chatbot_data.to_csv(r'符合3个条件原始日志.txt',
                    header=None, index=False)
result.to_csv(r'符合3个条件处理后4个字段（去重）.txt',
              index=False)
# result = pd.read_csv(r'符合3个条件处理后4个字段.txt', dtype='str')

result = result.drop_duplicates()  # 去重
tmp = result.groupby(by=['code', 'brand', 'term'])['mobileno'].count()  # 去重后统计
tmp = tmp.reset_index(drop=False)


# 3、分省匹配
prov_code = pd.read_excel(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\【5G消息】\5G消息各大区省份编码.xlsx',
                          names=['code', 'prov'])  # “编码-省份”映射表
tmp2 = pd.merge(tmp, prov_code, on='code')  # code字段匹配省份信息
tmp2.to_excel(r'汇总统计.xlsx', index=False)
