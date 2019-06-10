def first_one_first_time(strings):
    lettet_count = {}
    for letter in strings:
        lettet_count[letter] = lettet_count.get(letter,0) + 1
    for letter in strings:
        if lettet_count[letter] == 1:
            return letter
        else:
            continue


if __name__ == '__main__':
    strings = input("输入需要检查的字符串：")
    letter = first_one_first_time(strings)
    print(letter)
