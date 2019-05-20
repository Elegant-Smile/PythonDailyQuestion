msg = input('请输入一个不多于5位的正整数>>>')
num = int(msg)
n = len(msg)
print("该数字是 {} 位数".format(n))
for i in range(n):
    single_num = num % 10
    print(single_num)
    num = num // 10
