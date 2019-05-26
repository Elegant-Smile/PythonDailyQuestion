def cal_sum(init_num, n):
    sum = 0
    for i in range(init_num, n + 1, 2):
        print('1/%d + ' % i if i < n else '1/%d = ' % i, end='')
        sum += 1 / i
    print('', sum)


if __name__ == '__main__':
    num = int(input("请输入一个数字:"))
    if num % 2 == 0:
        init_num = 2
        cal_sum(init_num, num)
    else:
        init_num = 1
        cal_sum(init_num, num)
