n = int(input("输入参与人数："))
steps, num_list = 3, list(map(int, list(range(1, n + 1))))
step, num_list_bk = steps - 1, num_list[:]


def ysfh(steps):
    global num_list, step
    out_number = num_list.pop(step)
    print("{} was killed!".format(out_number))
    step = step + steps
    while step >= len(num_list):
        step -= len(num_list)
    else:
        if len(num_list) == 1:
            pass
        else:
            ysfh(steps)


ysfh(steps)
print("最后一个存活的是{}号".format(num_list_bk.index(num_list.pop(0))))
