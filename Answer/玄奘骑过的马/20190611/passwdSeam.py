# _*_coding:utf-8 _*_
# Author:Oldyuan
# ChangeTime: 2019/6/11 9:56
# FileName: passwdSeam.py


# def userPasswd():
#
#     username = input('请输入用户名：')
#     userPassword = input('输入密码：')
#     return {username,userPassword}
#
# def yanzheng(username,userPassword):
#     NUM = 0
#     if username == "Kate" and userPassword == '666666' :
#         print("登录成功!")
#     else:
#         print(NUM)
#         userPasswd()
#
#         NUM += 1
#         if NUM >=3:
#             print("3次用户名或者密码均有误！退出程序。")

def userPasswd():
        num2 = 0
        for i in range(0,3):
            username = input('请输入用户名：')
            userPassword = input('输入密码：')
            if username == "kate" and userPassword == "666666":
                print("登录成功！")
                break
            else:
                num2 +=1
                if num2 >=3:
                    print("3次用户名或者密码均有误！退出程序。")
                continue

    # pass


if __name__ == "__main__":
    num = 1
    userPasswd()





