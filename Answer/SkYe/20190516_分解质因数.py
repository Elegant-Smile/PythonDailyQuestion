def find_faction(num, faction_list):
    try:
        if num > 1:
            for i in range(2, num + 1):  # 这里+1是因为最后一个质因数自身的因子只有1和本身
                if num % i == 0:
                    faction_list.append(i)
                    break
            find_faction(int(num / i), faction_list)
    except:
        print("{}error".format(num))


def main():
    while True:
        try:
            num = int(input("输入正整数："))
            if num <= 0:
                print("请勿输入零或负数")
                continue
            else:
                break
        except:
            print("请检查输入是否为正整数!")
    faction_list = []
    find_faction(num, faction_list)
    print("{}={}".format(num, '*'.join(list(map(str, faction_list)))))


main()
