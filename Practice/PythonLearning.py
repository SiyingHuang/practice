import json
path = r'D:\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\利用Python进行数据分析\pydata-book-2nd-edition\datasets\bitly_usagov\example.txt'
open(path).readline()
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

# 统计时区出现的次数
# （1）使用普通方法
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
counts = get_counts(time_zones)
# （2）使用字典初始化
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in counts:
        counts[x] += 1
    return counts

# 统计出现次数最多的时区
# 法1
def top_counts(count_dict, n):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
top_counts(counts, n=10)
# 法2
from collections import Counter
counts = Counter(counts).most_common(10)
# 法3：用pandas
import pandas as pd
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
tz_counts[:10]

# 绘制图像（在pylab模式下才能生效，已尝试在ipython可绘制图像）
clean_tz = frame['tz'].fillna('Missing')
clean_tz.loc[clean_tz == ''] = 'Unknown'  # 或写成clean_tz[clean_tz == ''] = 'Unknown'
clean_tz.value_counts()[:10].plot(kind='barh', rot=0)

# frame中的a字段
# 解析USER_AGENT字符串信息（即每行'a'字段中首个元素）
result = pd.Series(x.split()[0] for x in frame['a'].dropna())
result[:5]
result.value_counts()[:3]
# 统计不同时区所使用的操作系统
import numpy as np
cframe = frame.loc[frame.a.notnull()]
operating_system = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])  # 分组结果
agg_counts = by_tz_os.size().unstack().fillna(0)  # size()相当于Series的value_counts()，进行计数
indexer = agg_counts.sum(1).argsort()  # 时区出现的次数并升序排列，argsort()返回索引位置。。sum(0)表示按列相加，sum(1)表示按行相加。
count_subset = agg_counts.take(indexer)[-10:]  # 最常出现的10个时区的Windows操作系统使用情况（是否Windows）