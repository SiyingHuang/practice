# 【Lesson3 练习】
# 1、检查输入
def int_check():
    while True:
        var = input('请输入一个0-9之间的整数：')
        if var.isnumeric():
            if (int(var) >=0) & (int(var) <= 9):
                break
            else:
                print('输入的整数超出0-9的范围，请重新输入。')
        else:
            print('您输入的不是整数，请重新输入。')

# 2、猜列表数字
import random
def int_game():
    setInt = random.sample(range(9), 3)
    print('您需要猜的数字，是一个[0. 9]之间的整数。')
    print('您有5次猜数机会。')
    for guessTimes in range(5):
        guessNum = int(input('请输入您猜的数字：'))
        if guessNum not in setInt:
            print('猜错了！')
        else:
            break
    if guessNum in setInt:
        if guessNum == setInt[0]:
            print('No.1')
        elif guessNum == setInt[1]:
            print('No.2')
        else:
            print('No.3')
    else:
        print('很遗憾，你的5次机会用完了。正确答案为：'+str(setInt))


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