variable = list(input("输入四个数字：（空格分隔）").split(' '))
x0,y0,x1,y1 = variable[0],variable[1],variable[2],variable[3]
distance = ((eval(x0)-eval(x1))**2 + (eval(y0)-eval(y1))**2)**0.5
print("{:.1f}".format(distance))
