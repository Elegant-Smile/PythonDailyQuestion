def faction(num):
    faction_list = []
    for i in range(1, num):
        if num % i == 0:
            faction_list.append(i)
    return faction_list


def main():
    for i in range(1, 1001):
        faction_list = faction(i)
        if sum(faction_list) == i:
            print("{}={}".format(i, '+'.join(list(map(str, faction_list)))))


main()
