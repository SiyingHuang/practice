import pandas as pd

with open(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\A组.txt') as f:
    for i in range(5):
        tmp = f.readline()
        print(tmp)

data1 = pd.read_csv(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\A组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'], encoding='GBK')
data1['zu'] = 'A'

data2 = pd.read_csv(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\B组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'], encoding='GBK')
data2['zu'] = 'B'

data3 = pd.read_csv(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\C组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'], encoding='GBK')
data3['zu'] = 'C'

data4 = pd.read_csv(r'C:\Users\Administrator\Desktop\Fw_Re_Native流失用户召回短信需求——文案测试批\D组.txt',
                    sep=',', header=None, usecols=[0], names=['mobileno'], encoding='GBK')
data4['zu'] = 'D'