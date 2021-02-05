# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/3
# @Author : Owen

import pandas as pd
import re
import time
import os
import sys


"""仅提取号码时"""
def extract_mobileno(s):
    pattern = re.compile(r'.*sip:\+86(\d*).*')
    gp = re.search(pattern, s)
    if gp:
        return gp.group(1)
    else:
        return 'else'


"""处理函数"""
def handler():

    print('开始处理..\n')
    st = time.time()

    """读取原始日志"""
    log_up = pd.read_csv(FILE, header=None, sep='sep@@', names=['ua'],
                         engine='python', chunksize=100000)

    chatbot_data = []
    """筛选出UP2.4终端日志"""
    print('1.根据已有条件，筛选日志..')
    for i in log_up:
        # UP2.4口径
        tmp = i.loc[(i['ua'].map(lambda x: 'UP_2.4' in x)) & (      # 含 “UP_2.4”
                     i['ua'].map(lambda x: 'Meiz' not in x)) & (    # 不含 “Meiz”
                     i['ua'].map(lambda x: 'GB' not in x))]         # 不含 “GB”
        chatbot_data.append(tmp)
    chatbot_data = pd.concat(chatbot_data, ignore_index=True)  # 不保留原始索引
    del log_up, tmp

    print('2.提取号码，完成去重..')
    result = pd.DataFrame(columns=['mobileno'])
    result['mobileno'] = chatbot_data['ua'].map(extract_mobileno)

    print('3.输出txt文件..\n')
    result.drop_duplicates().to_csv(os.path.join(PATH, (FILE_NAME + '（符合3个条件号码去重）.txt')), header=None, index=False)
    del result

    print('处理完成!\n耗时{:.4f}秒'.format(time.time() - st))


if __name__ == '__main__':
    FILE = sys.argv[1]
    FILE_NAME = FILE[:-4]
    PATH = os.path.dirname(FILE)
    handler()
