import numpy as np
import pandas as pd
import os
from datetime import datetime

pd.set_option('display.max_columns', 600)
pd.set_option('display.width', 300)

os.chdir(r'C:\Users\Administrator\Desktop\挖财')
cols = ['消费日期', '支出大类', '支出小类', '消费金额', '账户', '商家', '报销', '成员金额', '备注']
bill_ex = pd.read_excel(r'wacai_日常账本_202008261600179_732.xlsx', sheet_name='支出',
                        usecols=cols)
# 设置索引、构造字段
bill_ex['消费日期'] = bill_ex['消费日期'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))  # 格式化日期时间字段
bill_ex.index = bill_ex['消费日期'].map(lambda x: x.date())  # 将索引设为8位日期
bill_ex['year'] = bill_ex['消费日期'].map(lambda x: x.date().year)
bill_ex['month'] = bill_ex['消费日期'].map(lambda x: x.date().month)
bill_ex.info()

bill_ex.pivot_table('消费金额',
                    index='month', columns='支出大类',
                    aggfunc='mean',
                    fill_value=0)
