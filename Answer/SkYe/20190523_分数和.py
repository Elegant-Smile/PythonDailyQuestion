num = int(input("输入一个整数："))
if num%2 == 0:
    out_print = 0
    for i in range(2,num+1,2):
        out_print += 1/num
    print(out_print)
else:
    out_print = 0
    for i in range(1,num+1,2):
        out_print += 1/num
        print(out_print)
