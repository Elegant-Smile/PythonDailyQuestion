'''
用户输入一个字符串，修改该字符串中哪个位置的字符，程序就会输出修改后的结果。
比如用户输入 ：
字符串>> fkjava.org
字符位置>> 6
替换字符>> -
程序将会输出： 
替换后的字符串>> fkjava-org
'''
u_str = list(input('Input The Str: '))
p = int(input('字符位置: '))
r = input('替换字符: ')

u_str[p] = r

print(''.join(u_str))