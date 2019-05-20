num = input("请输入不大于五位数的数字：")
length = len(num)
print("{}是{}位数".format(num, length))
print("{}逆序后的数字为:{}".format(num, num[::-1]))
