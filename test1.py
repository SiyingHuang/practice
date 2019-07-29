import csv

csv_path = r'E:\学习\充电\Python学习\流失用户分析\test1.csv'
csv_file = csv.reader(open(csv_path,'r'))
print(csv_file)

data_ls = []
for line in csv_file:
    data_ls.append(line)

def count_active(data):
    counts = {}
    for line in data_ls:
        for x in line[]:
            counts[x]