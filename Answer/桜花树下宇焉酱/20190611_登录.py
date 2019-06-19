'''
给用户三次输入用户名和密码的机会，要求如下：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
1）如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬
2）当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。
'''
import sys
admin_username,admin_password = 'Kate','666666'
count = 0

while True:
	if count == 3:
		sys.exit()

	username = input('Input Your Username: ')
	password = input('Input Your Password: ')

	if all([username==admin_username, password==admin_password]):
		print('登录成功')
		sys.exit()
	else:
		print('用户名或密码错误\n')
		count += 1
