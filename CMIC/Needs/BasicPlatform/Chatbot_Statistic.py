# -*-coding:utf-8-*-


import pandas as pd
from datetime import datetime
import time
import os


def chatbot_statistic():
    st = time.time()
    print('任务开始！时间：{}'.format(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')))
    print('处理中，请稍候...')

    data = 