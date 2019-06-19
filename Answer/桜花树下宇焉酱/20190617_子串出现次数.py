'''
用户输入一个字符串和 一个子串，
程序必须打印出给定子串在目标字符串中出现的次数 。
字符串遍历将从左到右进行，而不是从右到左 。 
例如给定'ABCDCDC’和’CDC'，程序输出“ 2 ”。
'''


def count_str(u_str,s_str):
	count = 0
	for i in range(len(u_str)-1):
		if u_str[i:i+len(s_str)] == s_str:
			count += 1
	return count

if __name__ == '__main__':
	u_str = input('输入一个母字符串: ')
	s_str = input('输入一个子字符串: ')
	count = count_str(u_str,s_str)
	print(count)