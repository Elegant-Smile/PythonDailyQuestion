'''
列表中有一个数字出现的次数超过列表长度的一半，请找出这个数字。
例如，输入一个长度为 9 的列表[1, 2, 3, 2, 2, 2, 5, 4, 2]。
数字 2 出现了5次，超过列表长度的一半，因此输出2。
如果不存在则输出0。
'''
import random

t = []
lens = int(input('The len is :'))

for i in range(lens):
    t.append(random.choice(range(lens)))
print('数组为',t)

for i in list(set(t)):
	if t.count(i) > lens//2:
		print(i)