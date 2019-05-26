import math
print(".."*16)

x = int(input("请输入直角三角形的一条直角边的边长：\n"))
y = int(input("请输入另一条直角边的边长: \n"))

z = math.sqrt(x*x + y*y)
print(".."*16)
print("直角三角形的斜边长为：{}".format(z))
