#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
import re
import codecs


def nativedown(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        content = seg[3].split('&')
        msgid = content[0]
        sendnum = content[1]
        receivenum = content[2]
        code = content[4]
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip('tel:'))
        fw.write(',')
        fw.write(str(receivenum))
        fw.write(',')
        fw.write(msgid)
        fw.write(',')
        fw.write(code)
        fw.write('\n')

    f.close()
    fw.close()


def maapdown(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        msgid = re.search(r'maapBody[:](.){36}', log).group()
        sendnum = re.search(r'sip[:](.*?)com', log).group()
        receivenum = re.search(r'[+86]\d{11}', log).group()
        code = re.search(r'code[:](.){1,3}', log).group()
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip("sip:").rstrip("']"))     # 先后移除左侧（"sip:"）、右侧（"']"）指定字符
        fw.write(',')
        fw.write(str(receivenum).lstrip("['").rstrip("']"))
        fw.write(',')
        fw.write(str(msgid).lstrip("maapBody:").rstrip("']"))
        fw.write(',')
        fw.write(str(code).lstrip("code:").rstrip("']"))
        fw.write('\n')

    f.close()
    fw.close()


def downstate(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        msgid = re.search(r'messageId["][:]["](.*?)["]', log).group(0)
        sendnum = re.search(r'sip[:](.*?)com', log).group(0)
        receivenum = re.search(r'[+86]\d{11}', log).group(0)
        code = re.search(r'deliveryStatus["][:]["](.*?)["]', log).group(0)
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip("sip:").rstrip("']"))
        fw.write(',')
        fw.write(str(receivenum).lstrip("['").rstrip("']"))
        fw.write(',')
        fw.write(msgid.lstrip('messageId').lstrip('":"').rstrip('"'))
        fw.write(',')
        fw.write(str(code).lstrip('deliveryStatus":"').rstrip('"'))
        fw.write('\n')

    f.close()
    fw.close()


def up(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        if re.search(r'messageId["][:]["](.*?)["]', log):
            msgid = re.search(r'messageId["][:]["](.*?)["]', log).group(0)
        else:
            msgid = 'null'
        receivenum = re.search(r'sip[:](.*?)com', log).group(0)
        sendnum = re.search(r'[+86]\d{11}', log).group(0)
        code = re.search(r'bodyText["][:]["](.*?)["]', log).group(0)
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip("sip:").rstrip("']"))
        fw.write(',')
        fw.write(str(receivenum).lstrip("['").rstrip("']"))
        fw.write(',')
        fw.write(msgid.lstrip('messageId').lstrip('":"').rstrip('"'))
        fw.write(',')
        fw.write(str(code).lstrip('bodyText":"').rstrip('"'))
        fw.write('\n')

    f.close()
    fw.close()


def recall(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        msgid = re.search(r'messageid["][:]["](.*?)["]', log).group(0)
        sendnum = re.search(r'from["][:]["](.*?)["]', log).group(0)
        receivenum = re.search(r'[+86]\d{11}', log).group(0)
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip('from').lstrip('":"').lstrip('sip:').rstrip('"'))
        fw.write(',')
        fw.write(str(receivenum).lstrip("['").rstrip("']"))
        fw.write(',')
        fw.write(msgid.lstrip('messageid').lstrip('":"').rstrip('"'))
        fw.write('\n')

    f.close()
    fw.close()


def recallstate(fname, fwname):
    f = open(fname, 'r')
    fw = open(fwname, 'w')
    logs = f.readlines()
    for log in logs:
        seg = log.split(',')
        time = seg[0]
        msgid = re.search(r'messageid["][:]["](.*?)["]', log).group(0)
        sendnum = re.search(r'from["][:]["](.*?)["]', log).group(0)
        receivenum = re.search(r'[+86]\d{11}', log).group(0)
        code = re.search(r'status["][:]["](.*?)["]', log).group(0)
        fw.write(time)
        fw.write(',')
        fw.write(str(sendnum).lstrip('from').lstrip('":"').lstrip('sip:').rstrip('"'))
        fw.write(',')
        fw.write(str(receivenum).lstrip("['").rstrip("']"))
        fw.write(',')
        fw.write(msgid.lstrip('messageid').lstrip('":"').rstrip('"'))
        fw.write(',')
        fw.write(str(code).lstrip('status":"').rstrip('"'))
        fw.write('\n')

    f.close()
    fw.close()


def main():
    fnativedown = './data/nativedown.txt'
    fmaapdown = './data/maapdown.txt'
    fdstate = './data/downstate.txt'
    fup = './data/up.txt'
    frecall = './data/recall.txt'
    frstate = './data/recallstate.txt'

    fwnativedown = './data/result/nativedown_t.csv'
    fwmaapdown = './data/result/maapdown_t.csv'
    fwdstate = './data/result/downstate_t.csv'
    fwup = './data/result/up_t.csv'
    fwrecall = './data/result/recall_t.csv'
    fwrstate = './data/result/recallstate_t.csv'

    # f1.write(codecs.BOM_UTF8)

    # native down ---------------------------------------
    nativedown(fnativedown, fwnativedown)


# maap down ---------------------------------------
#     maapdown(fmaapdown,fwmaapdown)

# down state ---------------------------------------
#     downstate(fdstate,fwdstate)

# up ---------------------------------------
#     up(fup,fwup)

# recall ---------------------------------------
#     recall(frecall,fwrecall)

# recall state ---------------------------------------
#     recallstate(frstate,fwrstate)

if __name__ == '__main__':
    main()
