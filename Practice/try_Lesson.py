import pandas as pd
import numpy as np

while True:
    num = input('请输入一个0-9之间的整数：')
    if not num.isnumeric():
        print('不是整数，请重新输入。', end='')
    elif not (0 <= int(num) <= 9):
        print('不是0-9之间，请重新输入。', end='')
    else:
        print('您输入的整数为:{}'.format(int(num)))
        break

# 猜随机数
import random
rand_ls = random.sample(range(10), 3)
while True:
    num = input('随机数位于0-9之间，请猜数：')
    if int(num) not in rand_ls:
        print('猜错了，输入1继续，否则输入2退出游戏。')
        break
    else:
        for guess_num in rand_ls:
            if num == guess_num:
                print('获得第{}名'.format(rand_ls.index(guess_num)))