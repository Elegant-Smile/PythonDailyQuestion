'''
809*x=800*x+9*x
	1.x代表的是两位数
	2.8*x的结果为2位数
	3.9×x的结果为3位数
求x及809×x结果
'''

for x in range(10,100):
	if (10<=8*x<=100) and (100<=9*x<=1000):
		print(809*x)
# 9708