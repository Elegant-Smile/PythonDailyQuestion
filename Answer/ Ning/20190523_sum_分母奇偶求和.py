def sum(n):
    sum_even = 0
    sum_odd = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_even += 1 / i
        else:
            sum_odd += 1 / i
    if n % 2 == 0:
        print(sum_even)
    else:
        print(sum_odd)


if __name__ == '__main__':
    n = int(input("请输入n的值："))
    sum(n)
