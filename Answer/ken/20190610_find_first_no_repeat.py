def find_first_no_repeat(my_str: str) -> str:
    temp = []
    re_temp = []
    for ch in my_str:
        if ch not in temp:
            temp.append(ch)
        else:
            re_temp.append(ch)
    for ch in temp:
        if ch not in re_temp:
            return ch


if __name__ == '__main__':
    string_input = input("请输入字符串：")
    first_no_repeat_letter = find_first_no_repeat(string_input)
    print("%s 中 第1个只出现1次的字符是 %s" % (string_input, first_no_repeat_letter))