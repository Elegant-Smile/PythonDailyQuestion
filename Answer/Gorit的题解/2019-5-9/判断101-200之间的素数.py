#判断101 到 200 之间的素数
# 思路一：用平方根的方式
import math
def judge(num):
    for i in range(2,(int)(math.sqrt(num))):
        if num%i==0:
            return 0
        else:
            return 1#是素数
def PrimeNum(n,m):
    for i in range(n,m):
        if judge(i) == 1:
            print(i)
        else:
            continue
n,m=101,200
PrimeNum(n,m)

#思路二：直接用101~200之间（i）的每个数去整除从 2到i-1，如果能整除就不是素数，不能就不是素数
for i in range(101,200):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
            break
