""""
詹承宗-Python课程、练习等。
"""


import pandas as pd
import numpy as np
import os

# 【利用Python进行简单文本分析】
from datetime import datetime
# 1、处理格式异常的日志
os.chdir(r'D:\Data\中移互联网\01 - 运营室\01 - 分析组\05 - 充电\Python\[承宗]-Python课程\利用Python进行简单文本分析\文本分析_mm-pandas\文本分析')
handle_txt = open('handle.txt', 'w', encoding='utf-8')
with open('文件1：40123端口用户上行消息.csv', 'r', encoding='gbk') as f:
    for idx, line in enumerate(f):
        if idx <3:
            continue
        while True:
            last_element = line.split(',')[-1].replace('\n', '')  # 每行最后一个元素

            try:
                datetime.strptime(last_element, '%Y-%m-%d %H:%M:%S')
            except:
                line = line.replace('\n', '') + f.readline()
                continue

            if line.count(',') == 3:
                handle_txt.write(line)
            else:
                ls = line.split(',')

                # ls[1:-2]为消息内容所在位置，将内容中的英文逗号替换为中文逗号
                new_line = ls[0] + ',' + '，'.join(ls[1:-2]) + ',' + ls[-2] + ',' + ls[-1]
                handle_txt.write(new_line)
            break

handle_txt.close()




# 【Lesson4 练习】
# 1、判断两个字符串是否相同
def is_equal(var1, var2):
    if not (isinstance(var1, str) & isinstance(var2, str)):
        return None
    if len(var1) != len(var2):
        return False
    for i in range(len(var1)):
        if var1[i] != var2[i]:
            return False
    return True
print(is_equal('abc', 10))
print(is_equal('01', '10'))
print(is_equal('ab', 'ab'))
# 2、返回满足条件的两数之和的下标
def two_sum(nums, sum):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == sum:
                return [i, i+1]
print(two_sum([1,2,3,4,5], 9))



# 【Lesson3 练习】
# 1、检查输入
def int_check():
    while True:
        num = input('请输入一个0-9之间的整数：')
        if not num.isnumeric():
            print('不是整数，请重新输入。', end='')
        elif not (0 <= int(num) <= 9):
            print('不是0-9之间，请重新输入。', end='')
        else:
            print('您输入的整数为:{}'.format(int(num)))
            break
# 2、猜列表数字
import random
# 自己尝试（存在问题：只有猜错时，才能选择是否继续游戏）
while True:
    rand_ls = random.sample(range(10), 3)
    num = int(input('随机数位于0-9之间，请猜数：'))
    if int(num) not in rand_ls:
        print('猜错了 o(╥﹏╥)o \n --随机列表为{}'.format(rand_ls))
        enter = int(input('输入1继续，输入其他则退出游戏。'))
        if enter == 1:
            continue
        else:
            break
    else:
        for guess_num in rand_ls:
            if num == guess_num:
                print('猜对了，获得第【{}】名 (*^▽^*) \n --随机列表为{}'.format(rand_ls.index(guess_num)+1, rand_ls))
    break
    enter = int(input('输入1继续，输入其他则退出游戏。'))
    if enter == 1:
        continue
    else:
        break
# 参考答案
def int_game():
    rewards = ['第一名', '第二名', '第三名']
    print('您需要猜的数字，是一个[0-9]之间的整数。')
    while True:
        rand_ls = random.sample(range(10), 3)
        guessNum = input('请输入您猜的数字：')
        for guessTimes in range(3):
            if int(guessNum) == rand_ls[guessTimes]:
                print('随机列表为{}, 您获得了{}。'.format(rand_ls, rewards[guessTimes]))
                break
        else:
            print('随机列表为{}, 您没有获奖。'.format(rand_ls))
        ans = input('是否继续猜？ 按1重新开始，按2结束游戏。')
        if int(ans) == 1:
            pass
        elif int(ans) == 2:
            break



# 【Lesson2 练习】
# 1、列表操作
list1 = list(('apple', 'pear', 'orange'))
list1[:2]
list1.insert(1, 'coconut')
list1.pop(2) # 或list1.remove('apple')
'apple' in list1
# 2、字典操作
dict1 = {u'小明': '1990-1-1', u'小红': '2000-1-1', u'小王': '2010-1-1'}
dict1['小红']
dict1['小王'] = '2010-12-12'
'小明' in dict1  # 或'小明' in dict1.keys()
dict1.values() == '2020-10-1'  # '2020-10-1' in dict1.values()



# 【Lesson1 练习】
# 1、交互式输入与格式化输出
def user_info():
    name = input('姓名：')
    sex = input('性别（男/女）：')
    while True:
        try:
            age = float(input('年龄：'))
            break
        except ValueError:
            print('年龄格式不正确，请重新输入。')
    print('您的姓名是：{}\n您的性别是：{}\n您是{}年出生的。'.format(name, sex, 2019 - int(age)))
# 2、字符串操作
# （1）
import re
str1 = 'My name is LiLei'
str2 = 'mY life is great'
str3 = 'my favorite food is salad！'
str_list = [str1, str2, str3]
str = ', '.join(str_list)
str = '%s, %s, %s' %(str1,str2,str3)
# （2）
re.findall('my', str, re.IGNORECASE)
str2 = re.sub('my', 'your', str, flags=re.IGNORECASE)
#（3）
str2.count('is')