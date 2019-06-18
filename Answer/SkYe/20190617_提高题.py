num_1 = int(input('>>'))
num_2 = int(input('>>'))
while True:
    if num_2 != 0:
        num_ing = num_1 ^ num_2  # 处理不进位；不进位信息暂时赋值给num_ing，以免影响进位信息提取
        num_2 = (num_1 & num_2) << 1  # 处理进位；
        num_1 = num_ing  # 不进位信息赋值给num_1，在下一轮循环中合并不进位和进位
        # 循环直到合并num_1和num_2过程中不在出现进位，也就是num_2==0
    else:
        print(num_1)
        break
