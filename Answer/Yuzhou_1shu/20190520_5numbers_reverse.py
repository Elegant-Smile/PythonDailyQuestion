__author__ = "Yuzhou_1shu"


number = input("请输入一个不多于5位的正整数：")
if len(number) > 5 or int(number) < 0:
    print("Error, 请输入一个不多于5位的正整数：")
else:
    print("输入正整数的长度为：", len(number))
    print("逆序打印出各位数字", number[::-1])