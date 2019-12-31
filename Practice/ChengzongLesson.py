import pandas as pd
import numpy as np

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
        var = input('请输入一个0-9之间的整数：')
        if not var.isnumeric():
            print('您输入的不是整数，请重新输入。')
        else:
            if (int(var) >=0) & (int(var) <= 9):
                print('你输入的整数为{}'.format(var))
                break
            else:
                print('输入的整数超出0-9的范围，请重新输入。')
# 2、猜列表数字
import random
def int_game():
    rewards = ['第一名', '第二名', '第三名']
    print('您需要猜的数字，是一个[0-9]之间的整数。')
    while True:
        setInt = random.sample(range(10), 3)
        guessNum = input('请输入您猜的数字：')
        for guessTimes in range(3):
            if int(guessNum) == setInt[guessTimes]:
                print('随机列表为{}, 您获得了{}。'.format(setInt, rewards[guessTimes]))
                break
        else:
            print('随机列表为{}, 您没有获奖。'.format(setInt))
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