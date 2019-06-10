import math

s1 = input("请输入2个点坐标，用逗号分隔")
lst = s1.split(',')

x0 = int(lst[0])
y0 = int(lst[1])
x1 = int(lst[2])
y1 = int(lst[3])

a1 = int(pow((x0 - x1),2))
a2 = int(pow((y0 - y1),2))
leng = math.sqrt(a1 + a2)


print("({0},{1})，({2},{3})之间的距离为{4}" .format(x0,y0,x1,y1,leng))
