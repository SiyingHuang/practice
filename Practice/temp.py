import pandas as pd
import numpy as np
import datetime

with open(r'C:\Users\Administrator\Desktop\MIUI10_0818_fjm.txt', encoding='utf-8') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\fjmpp902\huawei9_0818_fjm.txt',
                   header=None)
data = pd.read_csv(r'C:\Users\Administrator\Desktop\fjmpp902\MIUI10_0818_fjm.txt',
                   header=None)