# 判断 0-n 之间有几个奇数
def judge_odd_num(num):
    odd_num = []
    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_num.append(i)

    return odd_num


def calc_odd_nums(num, odd_num_count):
    '''
    当一个数的最后一位为奇数时，那么这个数一定为奇数；
    首位肯定不为0；
    从该数为1位数到该数为(n+1)位数开始统计奇数的个数：
    1.当只有一位数时，奇数个数为 0-n之间的奇数个数，此处以7为例，0-7之间有4个奇数；
    2.当该数为两位数时，奇数个数为4*7=28, 首位有7个数的可能性，个位只有4个奇数可选；
    3.当该数为三位数时，奇数个数为：4*8*7=224，首位仍然是7个数，十位可以是0-7的任意一个数，即8个数的可能性，个位依旧
    以此类推。。。
    :param num: 输入的数字n
    :param odd_num_count: 0-n之间的奇数个数
    '''
    sum_odd_count = 0
    for i in range(1, num+1):
        if i == 1:
            odd_num_count = odd_num_count
        elif i == 2:
            first_place = num
            odd_num_count = odd_num_count * first_place
        if i > 2:
            odd_num_count *= num+1

        sum_odd_count += odd_num_count
        print('%d位数的奇数个数为%d' % (i, odd_num_count))

    print('0-%s所能组成的奇数个数总和为：%d' %(num, sum_odd_count))


if __name__ == '__main__':
    decimal_places = int(input("请输入数字n(1<n<10):"))
    odd_num = judge_odd_num(decimal_places)
    odd_num_count = len(odd_num)
    calc_odd_nums(decimal_places, odd_num_count)
