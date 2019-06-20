'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
print('exp整数数组:123456')
int_list = list(input('Input The Integer Array:'))
even_list = [] # 偶数

for i in int_list:
	if int(i)%2 == 0:
		int_list.remove(i)
		even_list.append(i)

int_list.extend(even_list)
print(int_list)