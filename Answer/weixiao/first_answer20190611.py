# 给定任意一个整数，打印出该整数的十进制、八进制、十六进制（大写）、二进制形式的字符串。

num = input('please input a number>>>')
dec_num = int(num)
print(dec_num)
print(oct(dec_num))
print(hex(dec_num).upper())
print(bin(dec_num))


# 给用户三次输入用户名和密码的机会，要求如下：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬

# 1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬

# 当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”

def check():
    n = 0
    while n < 3:
        name = input('>>>')
        password = input('>>>>')
        if name == 'Kate' and password =='666666':
            print('登录成功')
            break
        else:
            n += 1
if __name__ == '__main__':
    check()
