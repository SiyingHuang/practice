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