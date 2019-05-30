def replace_black(string):
	return string.replace(" ","%20")
def main():
	string=input('输入需要处理句子:')
	print(replace_black(string))
main()