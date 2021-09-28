# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/4
# @Author : Owen


class Employee:  # 员工基类
    empCount = 0  # 员工数

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' %Employee.empCount)

    def displayEmployee(self):
        print('name:', self.name, 'age:', self.age)


t1 = Employee('Mike', 16)  # 实例化
t2 = Employee('Tom', 23)
t1.displayEmployee()
t2.displayEmployee()
Employee.empCount

isinstance(t1, Employee)  # 判断是否为类的实例
