# 基础题：定义函数实现以下功能：求出 0-n 所能组成的奇数个数，
# 比如键盘输入n=7,求出0-7所能组成的奇数个数
n=eval(input('qingshuru'))
# 判断奇偶个数
def jiou(n):
    data=[]
    for i in range(1,n+1):
        if i % 2 !=0:
            data.append(i)
    return data
# 进行计算个数
def cal(n,count):
    sum=0
    for i in range(1,n+1):
        if i ==1:
            count=count
        elif i ==2:
            sum=n
            count=count*sum
        elif i>2:
            count*=n+1
            sum+=count
        print('{}位数的奇数个数：{}'.format(i,count))
    print('0-{}所能组成的奇数总和：{}'.format(n,sum))
    return sum
j=jiou(n)
count=len(j)
print(cal(n,count))


# 提高题：有如下分数序列： 2/1 ， 3/2 ， 5/3 ， 8/5 ， 13/8 ， 21/13...
# 求出这个数列的前 N 项之和，N由键盘输入
def sum(n):
    x,y,i,j=1,2,0,0
    while i<n:
        j+=y/x
        x,y=y,x+y
        i+=1
    return j
n=eval(input('qingshuru'))
print('{:.2f}'.format(sum(n)))
