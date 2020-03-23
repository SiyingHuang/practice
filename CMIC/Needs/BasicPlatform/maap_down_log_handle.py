# -*-coding:utf-8-*-

import pandas as pd
import re
from datetime import datetime
import time
import os


st = time.time()
os.chdir(r'C:\Users\Administrator\Desktop\关于消息中台日志规范输出的需求\规范日志示例\data')
"""pattern为正则表达式对象（正则对象）：便于复用，让程序更加高效"""
pattern = re.compile(r'(.{19}).*?sip:(\d*).*?\+86(\d*).*?maapBody:(.*?) code:(\d*).*',  # 每个括号中的内容代表一个分组
                     re.DOTALL)  # re.DOTALL，让'.'特殊字符匹配任何字符（包括换行符）
mp_time_l, main_l, called_l, msg_id_l, code_l = [], [], [], [], []
with open(r'maapdown.txt', 'r',
          encoding='utf-8') as f:
    for s in f:
        gp = pattern.search(s)
        if gp:
            # gp.group()  # 匹配正则表达式的整体结果（或group(0)）
            mp_time_l.append(gp.group(1))  # (.{19}).*?：取前19位字符（任意字符，因已注明DOALL）
            main_l.append(gp.group(2))     # sip:(\d*).*?：非贪婪方式（匹配尽量少的字符），匹配出“sip:”及其后边的数字
            called_l.append(gp.group(3))   # \+86(\d*).*?：非贪婪方式，匹配出“+86”及其后边的数字
            msg_id_l.append(gp.group(4))   # maapBody:(.*?)：非贪婪方式，匹配出“maapBody”及其后边的数字
            code_l.append(gp.group(5))     # code:(\d*).*：匹配出“code:”及其后边的数字，以及数字后边的任意字符
        else:
            mp_time_l.append(None)
            main_l.append(None)
            called_l.append(None)
            msg_id_l.append(None)
            code_l.append(None)

pd.set_option('display.max_columns', 300)
pd.set_option('display.width', 600)
data_output = pd.DataFrame({'mp_time': mp_time_l,
                          'main': main_l,
                          'called': called_l,
                          'msg_id': msg_id_l,
                          'code': code_l})
data_output.to_csv(r'maapdown_result.txt', header=None, index=False)

print('本次耗时{:.1f}秒'.format(time.time() - st))


# 优化后（修改每条日志解析后的插入方式为append）【问题：比优化前耗时更长】
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


# 自己写的日志处理脚本【问题：对每一行记录进行多次搜索，且每次搜索完成后都需要转换成Series格式，耗时长】
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


# 国曦提供的日志处理脚本
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