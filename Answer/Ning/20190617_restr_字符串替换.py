'''
用户输入一个字符串，修改该字符串中哪个位置的字符，程序就会输出修改后的结果。
比如用户输入 ：
字符串>> fkjava.org
字符位置>> 6
替换字符>> -
程序将会输出：
替换后的字符串>> fkjava-org
'''


def restr(ols, position, middle):
    s = list(old)
    # print(s)
    s[position] = middle
    # print(s)
    new = ''.join(s)
    print(new)


if __name__ == '__main__':
    old = input('please input:')
    position = int(input('please input:'))
    middle = input('please input:')
    restr(old, position, middle)
