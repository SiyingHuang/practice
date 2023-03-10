import numpy as np
import pandas as pd
import os
from datetime import datetime

pd.set_option('display.max_columns', 600)
pd.set_option('display.width', 300)

# 1、读取账单数据
os.chdir(r'C:\Users\Administrator\Desktop\挖财记账账单数据\导出时间：截至201912')
cols = ['消费日期', '支出大类', '支出小类', '消费金额', '账户', '商家', '报销', '成员金额', '备注']
bill_ex = pd.read_excel(r'日常账本_截至201912.xlsx', sheet_name='支出',
                        usecols=cols)
bill_in = pd.read_excel(r'wacai_日常账本_截至201912.xlsx', sheet_name='收入',
                        usecols=cols)
# 2、设置索引、构造字段
bill_ex['消费日期'] = bill_ex['消费日期'].map(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))  # 格式化日期时间字段
bill_ex.index = bill_ex['消费日期'].map(lambda x: x.date())  # 将索引设为8位日期
bill_ex['年'] = bill_ex['消费日期'].map(lambda x: x.date().year)
bill_ex['月'] = bill_ex['消费日期'].map(lambda x: x.date().month)
bill_ex['日'] = bill_ex['消费日期'].map(lambda x: x.date().day)
bill_ex = bill_ex[['消费日期', '年', '月', '日', '支出大类', '支出小类', '消费金额', '账户', '商家', '报销', '成员金额', '备注']]


# 3、pivot_table
bill_us = bill_ex.loc[bill_ex['成员金额'].map(lambda x: '小只❤大只' in x)]  # 小只大只账单
bill_us.pivot_table('消费金额',
                    index=['年'], columns='支出大类',
                    aggfunc='sum')

bill_ex.loc[bill_ex['成员金额'].map(lambda x: '小只❤大只' in x) & (
        bill_ex['支出小类'] == '电影') & (
                bill_ex['消费日期'].map(lambda x: x.date().year == 2015))][['消费日期', '支出小类', '商家', '成员金额', '备注']]  # 统计看电影情况
