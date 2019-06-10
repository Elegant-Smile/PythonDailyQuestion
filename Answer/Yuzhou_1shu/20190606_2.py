'''
请实现一个函数用来判断字符串是否表示数值(包括整数和小数)。例如，字符
串"+100","5e2",-123","3.141 6"和"-1E-16"都表示数值。但
是"12e","1a3.14","1 .2.3","+-5"和"12e+4.3"都不是。
'''


def is_Number(s):
    try:
        num = float(s)
        return True
    except:
        return False


if __name__ == '__main__':
    s = input("请输入一个字符串：")
    print(is_Number(s))
