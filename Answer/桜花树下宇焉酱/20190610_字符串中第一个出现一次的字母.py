# 请实现一个函数用来找出字符串中第1个只出现1次的字符。
# 例如，
# 当从字符串中只读出前两个字符"go"时，第1个只出现次的字符是"g"。
# 当从该字符串中读出前六个字符"google"时，第1个只出现1次的字符是“l”。

import sys
a = input('input the word:')
for a1 in a:
	if a.count(a1) == 1:
		print('第一个只出现一次的字符为{}'.format(a1))
		sys.exit()
print('没有只出现一次的字符')