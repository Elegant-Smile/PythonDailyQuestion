'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法
注：先后次序不同 算作是不同的结果
'''

def jump(n):
	if n == 1 or n == 2:
		return n
	return jump(n-1) + jump(n-2)

if __name__ == '__main__':
	print(jump(8))
