'''
求出任意非负整数区间中1出现的次数，
比如，1~13中包含1的数字有1、10、11、12、13，1~13的整数中1出现的次数是6次。
那100~1300的整数中1出现的次数是多少呢？
'''

def count(a=100,b=1300):
	count = 0
	for i in range(a,b+1):
		if '1' in str(i):
			# print(i)
			count += str(i).count('1')
	return count

if __name__ == '__main__':
	a,b = 100,1300
	count_num = count(a,b)
	print('{}~{}的整数中1出现的次数为:{}'.format(a,b,count_num))