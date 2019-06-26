# -*- coding:utf-8 -*-
# Author: chengbin_luo

'''
有如下分数序列： 2/1 ， 3/2 ， 5/3 ， 8/5 ， 13/8 ， 21/13... 求出这个数列的前 N 项之和，N由键盘输入
'''


def sum_fraction(n):
    x, y, i, j = 1, 2, 0, 0
    while i < n:
        j += y/x
        x, y = y, x+y
        i += 1
    return j


n = eval(input('请输入：'))
print('{:.2f}'.format(sum_fraction(n)))


