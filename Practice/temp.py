import pandas as pd
import numpy as np

with open(r'C:\Users\Administrator\Desktop\qiyuan_msg.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

gro = data_xiaomi.groupby('term')
gro.describe()

