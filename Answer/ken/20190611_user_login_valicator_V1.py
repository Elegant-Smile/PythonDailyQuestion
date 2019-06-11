login_count = 0


def user_valicator(fn):
    def print_user_name_password():
        global login_count
        user_name, user_pwd = fn()
        if user_name == "Kate" and user_pwd == "666666":
            exit("恭喜你登录成功！！！")
        else:
            login_count += 1
            if login_count < 3:
                print("请重新输入。。。")
            else:
                print("3次用户名或者密码均有误！")

    return print_user_name_password


@user_valicator
def login():

    user_name = input("请输入用户名：")
    user_pwd = input("请输入密码：")
    return [user_name, user_pwd]


if __name__ == '__main__':
    max_trying_times = 3
    while login_count < max_trying_times:
        login()


# 结果测试
'''
登录失败测试：
	
请输入用户名：ken
请输入密码：123
请重新输入。。。
请输入用户名：ken123
请输入密码：k233
请重新输入。。。
请输入用户名：tom
请输入密码：345
3次用户名或者密码均有误！	
'''

'''
登录成功测试：

请输入用户名：Kate
请输入密码：666666
恭喜你登录成功！！！
'''