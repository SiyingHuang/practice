import pandas as pd
import numpy as np
import random

rewards = ['第一名', '第二名', '第三名']
while True:
    rand_ls = random.sample(range(10), 3)
    guess_num = input('请输入0-9的整数')
    for guess in range(3):
        if int(guess_num) == rand_ls[guess]:
            print('您获得了{} \n --列表为{}'.format(rewards[guess], rand_ls))
            break
    else:
        print('您没有猜对 \n 列表为{}'.format(rand_ls))
    enter = input('是否重新猜数？输入1继续，输入2退出。')
    if int(enter) == 1:
        pass
    elif int(enter) == 2:
        break


def list_add_end(L=[]):
    L.append('END')
    return L
print(list_add_end())