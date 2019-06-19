'''
用户随机输入 N 个大写字母，使用 dict 统计用户输入的每个字母的次数 。 
比如，输入：FUWAHUHSDFJYULFSDHJ
输出：{'F': 3, 'U': 3, 'W': 1, 'A': 1, 'H': 3, 'S': 2, 'D': 2, 'J': 2, 'Y': 1, 'L': 1}
'''
def nums(u_str):
	nums_dict = {}
	for i in u_str:
		nums_dict[i] = u_str.count(i)
	return nums_dict


if __name__ == '__main__':
	u_str = input('输入大写字母:').upper()
	
	nums_dict = nums(u_str)
	print(nums_dict)