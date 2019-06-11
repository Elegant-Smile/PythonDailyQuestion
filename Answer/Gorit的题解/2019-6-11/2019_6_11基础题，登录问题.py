# 基础题
# Date 2019-6-11
# 账号 Kate
# 密码 666666
def h1():
    n=0# 输入次数
    account,password="",""#初始化账号密码
    while n<=3:
        account =input("请输入用户名:")
        password =input("请输入密码:")
        if account == "Kate":
            if password == "666666":
                print("登录成功!!!")
                break
            else:
                print("密码错误")
        else:
            print("账号错误")

if __name__ == '__main__':
    h1()
