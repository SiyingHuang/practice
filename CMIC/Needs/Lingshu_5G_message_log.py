import numpy as np
import pandas as pd
import re
import time

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

log_09 = pd.read_csv(r'D:\中移互联网\01 - 运营室\01 - 分析组\01 - 工作内容\HN20201113\合并\UP0920201113010001.txt',
                     header=None, sep='sep@@', names=['ua'],
                     engine='python', chunksize=100000)
chatbot_data = []
for i in log_09:
    tmp = i.loc[(i['ua'].map(lambda x: 'UP_2.4' in x)) & (i['ua'].map(lambda x: 'Meiz' not in x))]
    chatbot_data.append(tmp)

print('耗时{:.4f}秒'.format(time.time() - st))

chatbot_data = pd.concat(chatbot_data, ignore_index=True)
chatbot_data['ua'].map(lambda x: re.search(pattern, x).groups())