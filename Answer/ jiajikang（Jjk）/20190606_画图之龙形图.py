"""
 author:jjk
 datetime:2019/6/7
 coding:utf-8
 project name:Pycharm_workstation
 Program function:
 
"""
import turtle as t
import time
import math

n = 10  # Number of folds
step = 10  # Step length
l = 2 ** n - 1
a = [0] * l
print("L is ", l)


def fold(m, start, end, dir):
    if (m <= n):
        c = start + math.floor((end - start) / 2)
        a[c] = dir
        # print(a)
        fold(m + 1, start, c - 1, 0)
        fold(m + 1, c + 1, end, 1)


fold(1, 0, l, 0)

t.speed(0)
t.forward(step)
for i in range(l):
    if (a[i] == 0):
        t.left(90)
    else:
        t.right(90)
    t.forward(step)

#t.exitonclick()
while (True):
    t.left(1)
