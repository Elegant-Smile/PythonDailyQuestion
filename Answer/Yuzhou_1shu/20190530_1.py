def invest(amount, rate, time):
    '''
    复利计算
    :return:
    '''
    print('本金:{}'.format(amount))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print('第{}年: ¥{}'.format(t, amount))


if __name__ == '__main__':
    amount = float(input("请输入资金:"))
    rate = float(input("请输入年利率:"))
    time = int(input("请输入投资时间:"))
    invest(amount, rate, time)
