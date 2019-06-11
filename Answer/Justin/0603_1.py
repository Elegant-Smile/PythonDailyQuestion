a. 输出所有 sh 开头的单词
def sh(str):
	for i in str:
		if i[:2] == "sh":
			print(i)

sh(sent)

b. 输出所有长度超过 4 个字符的词
def len4(str):
	for i in str:
		if len(i) >4:
			print(i)

len4(sent)
