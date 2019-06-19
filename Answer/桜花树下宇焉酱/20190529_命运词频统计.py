'''
1.对文件"命运.txt"进行字符频次统计，
并将所有字符按照频次高低排序，
将排序后的字符及其频次输出到文件"命运-频次排序.txt"

字符包括中文、英文、标点等，但不包括空格和回车
输出格式要求：
(1)字符与频次之间采用冒号 ：分隔
(2)一个字符一行，比如
理:224
斯:120 
卫:100
'''
# f = open(r'test.txt','r')
f = open(r'命运.txt','r')
m = f.read().replace('\n','')
target = {}

for word in m:
	target[word] = target.get(word,0) + 1
# print(target)

target = sorted(target.items(),key=lambda x:x[1],reverse=True)

with open('命运-频次排序.txt','w',encoding='utf8') as output:
	for tar,count in target:
		output.write('{}:{}\n'.format(tar,count))

f.close()

