def my_pow(x, n):
    return x ** n

from lib import m
from lib.cj_lesson import *

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
    print('您的姓名是：{}\n您的性别是：{}\n您是{}年出生的。'.format(name, sex, 2019-int(age)))

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