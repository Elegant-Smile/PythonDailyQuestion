'''
提高题：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。

'''
import random
x = []
n = int(input('数组长度为:'))

# 1. 生成数组
for i in range(n):
    x.append(random.choice(range(n)))
print('数组为',x)
# 2. 生成数组
# while len(x) != n:
	# x.append(random.choice(range(n)))
	# if len(x) == n:
		# break
		
# 输出第一个重复的数字               
for x1 in x:
	if x.count(x1) >= 2:
		print('第一个重复的数字为',x1)
		break