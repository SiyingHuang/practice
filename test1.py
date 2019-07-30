import csv
import pandas as pd
import collections

path_home = r'E:\学习\充电\Python学习\流失用户分析\test1.csv'
path_comp = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\流失用户分析\test1.csv'
csv_path = path_home
csv_path = path_comp

data_ls = pd.read_csv(path_comp)

csv_file = csv.reader(open(csv_path,'r'))
print(csv_file)

def count_active(data_ls):
    counts = collections.defaultdict(int)
    for line in data_ls:
        for x in line[1]:
            counts[line[0]] += 1
    return counts