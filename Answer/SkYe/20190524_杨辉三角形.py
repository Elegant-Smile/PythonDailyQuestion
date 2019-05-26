lines = int(input("请输入打印行数:"))
out_list, process_list = [1], [1]
if lines == 1:
    print('{}'.format(' '.join(list(map(str, out_list)))))
else:
    for j in range(lines):  # 行数
        print('{}'.format(' '.join(list(map(str, out_list)))))
        for i in range(1, j + 2):  # 下一行每行个数
            if i > len(out_list) - 1:
                process_list.append(1)
            else:
                process_list.append(out_list[i - 1] + out_list[i])
        out_list = process_list[:]
        process_list = [1]
