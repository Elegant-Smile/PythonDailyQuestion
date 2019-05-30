# 基础题：
# 设计一个复利计算函数invest（），它包含三个参数：amount（资金），
# rate（年利率），time（投资时间）。
# 键盘输入每个参数后，输出结果：返回每一年的资金总额
# 比如，amount = 10000 , rate = 8% ,time = 5
def invest(amount,rate,time):
    for i in range(1,time+1):
        sum=amount*(1+rate)**i
        print('第{}年总额为：{:.3f}'.format(i,sum))
    return sum
a=eval(input('请输入资金：'))
r=float(input('请输入年利率：'))
t=eval(input('请输入投资时间：'))
invest(a,r,t)


# 提高题：
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy，则经过替换之后的字符串为We%20Are%20Happy。
def change(t):
    i=t.replace(' ','%20')
    return i
j=str(input('请输入字符串：'))
print('替换后为：{}'.format(change(j)))
