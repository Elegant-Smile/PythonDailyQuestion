'''
有如下分数序列： 2/1 ， 3/2 ， 5/3 ， 8/5 ， 13/8 ， 21/13... 求出这个数列的前 N 项之和，N由键盘输入
'''
n = int(input("请输入N的值："))
sum = 0
num = 2
for i in range(1,n+1):

    sum += num / i
    num += i

print("前N位的值为：%f" % sum)


