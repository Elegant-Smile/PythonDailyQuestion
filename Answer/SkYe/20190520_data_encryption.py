while True:
    tele_num = input("输入电话号码：")
    if len(tele_num) == 4:  # 判断输入字符串位数
        try:
            if int(tele_num) >= 0:  # 判断是否为4位整数
                break
        except:
            pass
out_tele_num = []
for num in tele_num:
    num = (int(num) + 5) % 10
    out_tele_num.append(num)
for i in out_tele_num:
    print(i, end='')
print('')
print("{}".format(''.join(map(str, out_tele_num[::-1]))))
