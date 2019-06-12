temperature = input()
if temperature[-1].upper() == 'C':
    print("{:.2f}F".format(eval(temperature[:-1])*1.8+32))
elif temperature[-1].upper() == 'F':
    print("{:.2f}C".format((eval(temperature[:-1])-32)/1.8))
else:
    print("输入格式错误")