import pandas as pd
import glob


# 合并csv文件
def csv_combine():
    csv_list = glob.glob('*.csv')  # 查看文件夹下的csv文件数
    print(u'%s 个csv文件待合并。' % len(csv_list))
    print(u'正在处理...')
    for i in csv_list:
        fr = open(i, 'rb').read()  # 以二进制(b)格式打开一个文件用于只读(r)。
        print(u'正在处理文件：{}'.format(i))
        with open('combine_result.csv', 'ab') as f:  # 以二进制(b)格式打开一个文件用于追加(a)。
            f.write(fr)
    print(u'合并完毕！')


# 去重
def quchong(file):
    df = pd.read_csv(file, header=None)
    df_result = df.drop_duplicates()  # 默认drop_duplicates(subset=0)
    df_result.to_csv(file)


# 运行函数
if __name__ == '__main__':
    csv_combine()
    quchong('result.csv')
