'''
从键盘输入4个数字，各数字采用空格分隔，对应为变量x0,y0,x1,y1。
计算(x0，y0)和(x1,y1)两点之间的距离，输出结果保留1位小数。
比如，键盘输入：0 1 3 5，屏幕输出：5.0
'''
a = input('input your number:').split()
x0,y0,x1,y1 = int(a[0]),int(a[1]),int(a[2]),int(a[3])
target = float(((y0-y1)**2+(x0-x1)**2)**0.5)
print(target)
