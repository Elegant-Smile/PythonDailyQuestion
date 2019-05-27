def odd_number_combination(n):
    '''
    1.数字首位不能为0，可放数字为n个
    2.末位数字必须为奇数，可放数字为odd[1,n]个
    3.中间位数字任意，可放数字为n+1个
    :param n:0-9之间的数字
    :return:组成的奇数总数
    '''

    first = n
    last = len([x for x in range(n + 1) if x % 2 != 0])
    sum = last + first * last
    if n < 2:
        return sum
    for i in range(2, n + 1):
        middle = (n + 1) ** (i - 1)
        sum += first * middle * last

    return sum


if __name__ == "__main__":
    n = int(input('请输入一个0~n的数字:'))
    print(odd_number_combination(n))
