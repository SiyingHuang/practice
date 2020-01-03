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


