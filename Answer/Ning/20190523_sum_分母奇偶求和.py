n = int(input("请输入n的值："))
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += 1 / i
    else:
        sum_odd += 1 / i
print(sum_even)
print(sum_odd)
