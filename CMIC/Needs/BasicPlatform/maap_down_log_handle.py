# -*-coding:utf-8-*-

maapdown = pd.read_csv(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data\maapdown\maapdown_demo.txt',
                       header=None, dtype={2: 'str'})
maapdown.iloc[:, [2]]
str_demo = '2020-02-26 10:29:30.030,sip:12520040106@botplatform.rcs.chinamobile.com,+8613414928948,{"address":"+8613414928948","appid":"Uchatbot1252004010","bodyText":"--next\r\nContent-Type: application/vnd.gsma.botmessage.v1.0+json\nContent-Length: 1300\n\n{\"message\":{\"generalPurposeCardCarousel\":{\"content\":[{\"description\":\"亲爱的用户，您的手机已全面支持短信小程序。点击下方按钮，可以快速了解小程序、体验精品小程序、了解疫情最新动态！【中移互联网 增强信息】\",\"media\":{\"height\":\"MEDIUM_HEIGHT\",\"mediaContentType\":\"image/jpeg\",\"mediaUrl\":\"http://117.161.4.174/group/M00/B0/9B/CgIRnV4hE3uAE-mvAAP9_1HEnPo386.png\",\"thumbnailContentType\":\"image/png\",\"thumbnailUrl\":\"http://117.161.4.174/group/M00/B0/9B/CgIRnV4hE3uAE-mvAAP9_1HEnPo386_small.png\"},\"suggestions\":[{\"reply\":{\"displayText\":\"认识小程序\",\"postback\":{\"data\":\"认识小程序\"}}}],\"title\":\"【欢迎体验短信小程序】\"},{\"description\":\"为您推荐10086、火车票预订、违章代缴等三个精品短信小程序，马上了解一下吧\",\"media\":{\"height\":\"MEDIUM_HEIGHT\",\"mediaContentType\":\"image/jpeg\",\"mediaUrl\":\"http://117.161.4.174/group/M00/29/84/CgIRnV5V1vuADK6sAACu2vo9MB8735.png\",\"thumbnailContentType\":\"image/png\",\"thumbnailUrl\":\"http://117.161.4.174/group/M00/29/84/CgIRnV5V1vuADK6sAACu2vo9MB8735_small.png\"},\"suggestions\":[{\"reply\":{\"displayText\":\"精品小程序\",\"postback\":{\"data\":\"精品小程序\"}}}],\"title\":\"体验精品小程序\"}],\"layout\":{\"cardOrientation\":\"VERTICAL\",\"cardWidth\":\"MEDIUM_WIDTH\"}}}}\n--next\r\nContent-Type: application/vnd.gsma.botsuggestion.v1.0+json\nContent-Length: 265\n\n{\"suggestions\":[{\"reply\":{\"displayText\":\"认识小程序\",\"postback\":{\"data\":\"认识小程序\"}}},{\"reply\":{\"displayText\":\"精品小程序\",\"postback\":{\"data\":\"精品小程序\"}}},{\"reply\":{\"displayText\":\"共同战\\\"疫\\\"\",\"postback\":{\"data\":\"共同战\\\"疫\\\"\"}}}]}\n--next--","clientCorrelator":"12520040","contentType":"multipart/mixed; boundary=\"next\"","contributionID":"g302000003c68jzatn2a71799k72pahv8001","conversationID":"a1093c9f-cbc5-4e5e-a11b-fb58f8f56ea5","destinationAddress":"+8613414928948","imFormat":"IMPagerMode","messageId":"g302000003c68jzatn2a71799k72pahv8001","senderAddress":"sip:12520040106@botplatform.rcs.chinamobile.com","senderName":"A2p","subject":"统一消息接入平台","taskId":"439372507187773519"},201,maapBody:g302000003c68jzatn2a71799k72pahv8001 code:201'


import pandas as pd
import re
from datetime import datetime
import time
import os
import sys


def maap_down_log():
    FILE = r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data\maapdown\maapdown_demo.txt'
    l = []
    data = pd.read_csv(FILE, header=None, sep=',,,')
    st = time.time()
    for i in data.index:
        line = data.iloc[i][0]
        mp_time = pd.Series(datetime.strptime(line.split(',')[0][:-4], '%Y-%m-%d %H:%M:%S'))
        main = pd.Series(re.search(r'sip[:](.*?)[.]com', line).group().lstrip("sip:").rstrip(
            "@botplatform.rcs.chinamobile.com"))  # “.*?”匹配尽量少（?）的字符，非贪婪（一行中存在两个sip）
        called = pd.Series(re.search(r'[+86]\d{13}', line).group().lstrip("+86"))  # “\d”匹配任何十进制数(0-9)，共13个数字（含"+86"）
        msg_id = pd.Series(re.search(r'maapBody[:](.){36}', line).group().lstrip("maapBody:"))  # msg_id长度为36
        code = pd.Series(re.search(r'code[:](.){1,3}', line).group().lstrip("code:"))  # “code:”后的数字可能为1-3个
        line_s = pd.concat((mp_time, main, called, msg_id, code), axis=1)
        l = l.append(line_s)  # 因为line_s是DataFrame，所以要写成“l = l.append(xxx)”
    print('本次耗时{:.1f}秒'.format(time.time() - st))

def maap_down_log():
    FILE = r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data\maapdown\maapdown_demo.txt'
    l = []
    data = pd.read_csv(FILE, header=None, sep=',,,')
    st = time.time()
    mp_time_l = []
    main_l = []
    called_l = []
    msg_id_l = []
    code_l = []
    for i in data.index:

        line = data.iloc[i][0]
        mp_time = datetime.strptime(line.split(',')[0][:-4], '%Y-%m-%d %H:%M:%S')
        main = re.search(r'sip[:](.*?)[.]com', line).group().lstrip("sip:").rstrip(
            "@botplatform.rcs.chinamobile.com")  # “.*?”匹配尽量少（?）的字符，非贪婪（一行中存在两个sip）
        called = re.search(r'[+86]\d{13}', line).group().lstrip("+86")  # “\d”匹配任何十进制数(0-9)，共13个数字（含"+86"）
        msg_id = re.search(r'maapBody[:](.){36}', line).group().lstrip("maapBody:")  # msg_id长度为36
        code = re.search(r'code[:](.){1,3}', line).group().lstrip("code:")  # “code:”后的数字可能为1-3个

        mp_time_l.append(mp_time)  # 因为mp_time是List，因此要写成“mp_time_l.append(xxx)”
        main_l.append(main)
        called_l.append(called)
        msg_id_l.append(msg_id)
        code_l.append(code)

        line_s = pd.DataFrame((mp_time_l, main_l, called_l, msg_id_l, code_l))
    print('本次耗时{:.1f}秒'.format(time.time() - st))


st = time.time()
pattern = re.compile(r'(.{19}).*?sip:(\d*).*?\+86(\d*).*?maapBody:(.*?) code:(\d*).*', re.DOTALL)
mp_time_l, main_l, called_l, msg_id_l, code_l = [], [], [], [], []
with open(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data\maapdown\maapdown_demo.txt', 'r', encoding='utf-8') as f:
    for s in f:
        gp = pattern.search(s)
        if gp:
            mp_time_l.append(gp.group(1))
            main_l.append(gp.group(2))
            called_l.append(gp.group(3))
            msg_id_l.append(gp.group(4))
            code_l.append(gp.group(5))
        else:
            mp_time_l.append(None)
            main_l.append(None)
            called_l.append(None)
            msg_id_l.append(None)
            code_l.append(None)
print('本次耗时{:.1f}秒'.format(time.time() - st))

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 100)
test_data = pd.DataFrame({'mp_time': mp_time_l,
                          'main': main_l,
                          'called': called_l,
                          'msg_id': msg_id_l,
                          'code': code_l})








if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(r'输入参数有误，请重新输入！用法示例：')
    sys.exit(0)
    FILE = sys.argv[1]  # 传入第2个参数为待处理日志

    os.chdir(r'')
    maap_down_log()


def maapdown(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    str_demos = f.readlines()
    for str_demo in str_demos:
        seg = str_demo.split(',')
        time = seg[0]
        msg_id = re.search(r'maapBody[:](.){36}', str_demo).group()
        main = re.search(r'sip[:](.*?)com', str_demo).group()  # “.*?”匹配尽量少（?）的字符，非贪婪（一行中存在两个sip）
        called = re.search(r'[+86]\d{13}', str_demo).group()  # “\d”匹配任何十进制数(0-9)，共13个数字（含"+86"）
        code = re.search(r'code[:](.){1,3}', str_demo).group()  # “code:”后的数字可能为1-3个
        fw.write(time)
        fw.write(',')
        fw.write(str(main).lstrip("sip:").rstrip("@botplatform.rcs.chinamobile.com"))  # 先后移除左侧（"sip:"）、右侧（"@botplatform.rcs.chinamobile.com"）指定字符
        fw.write(',')
        fw.write(str(called).lstrip("+86"))
        fw.write(',')
        fw.write(str(msg_id).lstrip("maapBody:"))
        fw.write(',')
        fw.write(str(code).lstrip("code:"))
        fw.write('\n')

    f.close()
    fw.close()