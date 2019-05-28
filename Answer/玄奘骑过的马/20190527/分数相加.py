# -*- coding: utf-8 -*-
#Author:Oldyuan




n = int(input("请输入N的值："))
sum = 0
num = 2
for i in range(1,n+1):

    sum += num / i
    num += i

print("前N位的值为：%f" % sum)



