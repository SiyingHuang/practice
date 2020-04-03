import numpy as np
import pandas as pd
import re
import time
import os

pd.set_option('display.max_columns', 300)
pd.set_option('display.width', 600)
s = '[{"SurveyObjType":"3","QuestionTitle":"您有多大可能性向您的亲朋好友推荐和飞信？","Score":"10","SurveyLables":["不存在无法发送或接收不成功消息的情况"]},{"SurveyObjType":"3","QuestionTitle":"结合您在和飞信发送在线消息的情况，请您对和飞信的在线消息发送体验进行整体评价","Score":"10","SurveyLables":["消息发送正常"]}]'
s = '[{"SurveyObjType":"0","QuestionTitle":"装机整体满意度","Score":"10"},{"SurveyObjType":"2","QuestionTitle":"上门及时性","Score":"10"},{"SurveyObjType":"3","QuestionTitle":"安装专业性","Score":"10"},{"SurveyObjType":"2","QuestionTitle":"安装人员服务","Score":"10"},{"SurveyObjType":"0","QuestionTitle":"装机完成后是否测速","Score":"0","SurveyLables":["是"]},{"SurveyObjType":"0","QuestionTitle":"您是否知晓中国移动推出的“快装快修，超时送流量”活动？","Score":"0"},{"SurveyObjType":"0","QuestionTitle":"您本次装机服务是否比约定时间延迟？","Score":"0"},{"SurveyObjType":"0","QuestionTitle":"由于本次延迟上门，您获得了多少流量赠送？","Score":"0"}]'


gp = re.search(pattern, s)
gp.groups()
gp.group(1)
gp.group(2)


os.chdir(r'C:\Users\Administrator\Desktop')
data = pd.read_csv(r'nps_SurveyResult.txt', header=None, sep='|',
                   names=['mobileno', 'scene', 'content', 'date'])


pattern = re.compile(r'."(您有多大可能性向您的亲朋好友推荐.*?)","Score":"(\d*).*')

def extract_content(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(1)
    else:
        return 'else'


def extract_score(s):
    gp = re.search(pattern, s)
    if gp:
        return gp.group(2)
    else:
        return 'else'


def score_type(s):
    if 0 <= s <= 6:
        return '贬损'
    elif 7 <= s <= 8:
        return '中立'
    elif 9 <= s <= 10:
        return '推荐'
    else:
        return None


data['scene2'] = data['scene'].map(lambda x: str(x)[2:6])  # 取出场景编码（原始数据，如“["0058"]”）
data['ques'] = data['content'].map(extract_content)  # 取出NPS满意度调查的问题
data.loc[data.ques == 'else'].to_csv(r'no_ques.txt', header=None, index=False)  # 检查无此问题的日志
data = data.loc[~(data.ques == 'else')]  # 剔除无此问题的日志
data['score'] = data['content'].map(extract_score).astype(np.int8)
data['score_type'] = data['score'].map(score_type)
# data[['mobileno', 'scene2', 'ques', 'score', 'score_type']].to_csv(r'test.txt', header=None, index=False)
data[['mobileno', 'scene2', 'ques', 'score']].to_csv(r'npsMobilQuesScore.txt', header=None, index=False)

# 统计各场景、各满意度结果数量
data.scene2.drop_duplicates()  # 场景个数
result = data.groupby(by=['scene2', 'score_type']).count()['score'].to_frame().reset_index()
result.to_excel(r'各场景满意度结果.xls', index=False)
