x = input("请输入不小于5位的数字\n")
print(len(x))

for i in range(0,len(x)).__reversed__():
    print(x[i],end=" ")
