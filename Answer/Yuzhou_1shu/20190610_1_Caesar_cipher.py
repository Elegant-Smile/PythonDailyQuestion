def caesar_cipher(s):
    '''
    对输入字符串进行凯撒密码加密，直接输出结果
    空格不用进行加密处理
    :return:
    '''

    t = ""
    for c in s:
        if 'a' <= c <= 'z':  # str是可以直接比较的
            t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
        elif 'A' <= c <= 'Z':
            t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
        else:
            t += c
    return t


if __name__ == '__main__':
    s = input('请输入一个字符串：')
    print('凯撒加密后的密码：', caesar_cipher(s))
