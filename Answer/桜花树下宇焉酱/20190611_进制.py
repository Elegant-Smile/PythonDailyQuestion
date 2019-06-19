'''
给定任意一个整数，打印出该整数的十进制、八进制、十六进制（大写）、二进制形式的字符串。
'''
int_num = int(input('input the integer'))

# 转二进制
print('二进制形式为 : {}'.format(bin(int_num)))
# 转八进制
print('八进制形式为 : {}'.format(oct(int_num)))
# 转十进制
print('十进制形式为 : {}'.format(int(int_num)))
# 转十六进制
print('十六进制形式为 : {}'.format(hex(int_num).upper()))