num = int(input('请输入共多少人：'))
# 将所有人放入一个数组
list_count = list(range(1, num + 1))
# 设置一个变量，用于计算报数
count = 0
while len(list_count) > 1:  # 当数组中至少有2个元素时进行循环
    list_count_new = list_count[:]  # 把原数组拷贝到新数组中，用于限制内层循环次数
    for i in range(0, len(list_count_new)):  # 内层循环开始，从第一个人开始报数
        count = count + 1  # 每报一次，count计数器加1

        if count % 3 == 0:  # 如果count能被3整除，则是报到3的人
            print('第 {} 号淘汰'.format(list_count_new[i]))
            list_count.remove(list_count_new[i])  # 把报到3的人移除原数组，进行下一次循环

print('最后留下的是原来的第 {} 号'.format(list_count[0]))
