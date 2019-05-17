def summary():
    def recursion(n):
        if n == 1:
            return 1
        return n * recursion(n-1)

    lst = []
    for i in range(1, 21):
        list.append(recursion(i))
    print(sum(lst))  # 2561327494111820313


summary()