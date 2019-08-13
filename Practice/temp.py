import pandas as pd

filepath = r'C:\Users\Administrator\Desktop\副本小米12月有效结算核查（厂家有我方无）0806.xlsx'
data = pd.read_excel(filepath)

data.to_csv(r'C:\Users\Administrator\Desktop\副本小米12月有效结算核查（厂家有我方无）0806.txt',
            float_format=str, sep='|', header=None, encoding='utf-8')

