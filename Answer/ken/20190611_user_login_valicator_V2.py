def user_login_valicator(fn):
    global login_count
    login_count = 0
    
    def login_limit():
        global login_count
        while login_count < 3:
            user_valication_result = fn()
            if user_valication_result:
                exit("恭喜你登录成功！！！")
            else:
                login_count += 1
                if login_count < 3:
                    print("输入的账号或密码有误，请您重新输入！")
                else:
                    print("3次输入均有误！")
    return login_limit


@user_login_valicator
def login():
    user_name = input("请输入用户名：")
    user_pwd = input("请输入密码：")
    if user_name == "Kate" and user_pwd == "666666":
        return True
    else:
        return False


if __name__ == '__main__':
    login()
	
# 结果测试
'''
请输入用户名：Kate
请输入密码：666666
恭喜你登录成功！！！
'''

'''
请输入用户名：ken
请输入密码：123
输入的账号或密码有误，请您重新输入！
请输入用户名：ken
请输入密码：12345
输入的账号或密码有误，请您重新输入！
请输入用户名：Kate
请输入密码：1243
3次输入均有误！
'''