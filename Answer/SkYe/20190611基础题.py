def login(user_name, password):
    user_data = {'kate': '666666'}
    if user_name in user_data:
        if user_data[user_name] == password:
            return 'login'
        else:
            return 'password_error'
    else:
        return 'user_name error'


if __name__ == '__main__':
    counts = 0
    while counts < 3:
        user_name = input("请输入用户名：")
        password = input("请输入密码：")
        login_state = login(user_name, password)
        if login_state == 'user_name error':
            print('用户名不存在或错误，请重新输入。')
            counts += 1
        elif login_state == 'password_error':
            print('密码错误，请重新输入')
            counts += 1
        else:
            print('登录成功！')
            break
    else:
        print('3次用户名或者密码均错误！退出程序。')
