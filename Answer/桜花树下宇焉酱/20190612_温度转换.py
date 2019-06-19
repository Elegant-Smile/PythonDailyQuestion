'''
温度的刻画有两个不同体系：摄氏度（Celsius）和华氏度（Fahrenheit）。‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
请编写程序将用户输入华氏度转换为摄氏度，或将输入的摄氏度转换为华氏度。‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
转换算法如下：（C表示摄氏度、F表示华氏度）‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
         C = ( F - 32 ) / 1.8‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
         F = C * 1.8 + 32‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
要求如下：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
(1) 输入输出的摄氏度可采用大小写字母C结尾，温度可以是整数或小数，如：12.34C指摄氏度12.34度；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
(2) 输入输出的华氏度可采用大小写字母F结尾，温度可以是整数或小数，如：87.65F指摄氏度87.65度；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
(3) 输出保留小数点后两位，输入格式错误时，输出提示：输入格式错误；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
(4) 使用input()获得测试用例输入时，不要增加提示字符串。
'''

def change(t):
	if t[-1].upper() == 'C':
		t = float(t[:-1])*1.8+32
		print('%.2fF'%t)
	elif t[-1].upper() == 'F':
		t = float(t[:-1])-32/1.8
		print('%.2fC'%t)
	else:
		print('格式错误')
	
if __name__ == '__main__':
	# print('Exp:12.34C、87.65F')
	Temperature = input('The Temperature is:')

	change(Temperature)