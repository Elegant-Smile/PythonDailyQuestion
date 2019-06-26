# -*- coding:utf-8 -*-
# Author: chengbin_luo

# i = input('输入坐标').split()
# x1, x2, x3, x4 = eval(i[0]), eval(i[1]), eval(i[2]), eval(i[3])
# dis = pow((pow(x3 - x1, 2) + pow(x4 - x2, 2)), 0.5)
# print(dis)

# variable = list(input("输入四个数字：（空格分隔）").split(' '))
# x0,y0,x1,y1 = variable[0],variable[1],variable[2],variable[3]
# distance = ((eval(x0)-eval(x1))**2 + (eval(y0)-eval(y1))**2)**0.5
# print("{:.1f}".format(distance))


'''
从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1,y1。
计算(x0，y0)和(x1,y1)两点之间的距离，输出结果保留1位小数。
比如，键盘输入：0 1 3 5，屏幕输出：5.0
'''
# a = input('input your number:').split()
# x0, y0, x1, y1 = int(a[0]), int(a[1]), int(a[2]), int(a[3])
# target = float(((y0-y1)**2+(x0-x1)**2)**0.5)
# print(target)


import math

s1 = input("请输入2个点坐标，用逗号分隔")
lst = s1.split(',')

x0 = int(lst[0])
y0 = int(lst[1])
x1 = int(lst[2])
y1 = int(lst[3])

a1 = int(pow((x0 - x1), 2))
a2 = int(pow((y0 - y1), 2))
leng = math.sqrt(a1 + a2)


print("({0},{1})，({2},{3})之间的距离为{4}" .format(x0, y0, x1, y1, leng))