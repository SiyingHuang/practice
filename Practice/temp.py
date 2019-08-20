import pandas as pd


data.to_csv(r'C:\Users\Administrator\Desktop\副本小米12月有效结算核查（厂家有我方无）0806.txt',
            float_format=str, sep='|', header=None, encoding='utf-8')




filepath = r'C:\Users\Administrator\Desktop\【麻烦思颖协助抽样】RCS增强短信高价值NPS短信调研需求\24条+1000以上组.xlsx'
data = pd.read_excel(filepath, header=None, skiprows=1,
                     names=['mobileno', 'month', 'sum1', 'sum2'])

data_diaoyan = pd.read_excel(r'C:\Users\Administrator\Desktop\【麻烦思颖协助抽样】RCS增强短信高价值NPS短信调研需求\核心用户认知度调研号码（20190716）.xlsx',
                             header=None, skiprows=1,
                             names=['mobileno'])
data_diaoyan['tag1'] = 1

data_lingdao = pd.read_excel(r'C:\Users\Administrator\Desktop\【麻烦思颖协助抽样】RCS增强短信高价值NPS短信调研需求\中国移动部门领导以上号码20190116（汇总）.xlsx',
                             header=None,
                             names=['comp', 'mobileno'])
data_lingdao['tag2'] = 2

tmp = pd.merge(data, data_lingdao, how='left', on='mobileno')
tmp = tmp.loc[tmp['tag2'] != 2]
tmp = tmp.sample(n=180000)


tmp[['mobileno', 'month', 'sum1', 'sum2']].to_excel(r'C:\Users\Administrator\Desktop\【麻烦思颖协助抽样】RCS增强短信高价值NPS短信调研需求\[剔除后结果]24条+1000以上组（随机18W）.xlsx',
                                                    header=None, index=False)