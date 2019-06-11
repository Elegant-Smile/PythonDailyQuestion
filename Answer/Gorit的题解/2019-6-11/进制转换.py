# 进制转换 输入任意整数，打印其十进制，八进制，十六进制，二进制
# Python自带的
x = int(input("请输入一个数字"))
print("二进制{} 八进制{} 十进制{} 十六进制{}".format(bin(x),oct(x),x,hex(x)),end=",")
