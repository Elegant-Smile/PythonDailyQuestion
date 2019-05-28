# -*- coding: utf-8 -*-
#Author:Oldyuan
import math

def TheOddNumber():
    n = int(input('please input a number:'))
    s = 1
    sum =0
    for i in range(n+1):
        if i == 1:
            s = math.ceil(n/2)
            print('第一个s',s)
        elif i == 2:
            s = n * math.ceil(n/2)
            print('第二个s',s)
        else:
            s *=8
        sum +=s
        print('这个求和什么鬼',sum)
    # num = n *(n + 1)*ceil(n / 2)





if __name__ =="__main__":
    TheOddNumber()


