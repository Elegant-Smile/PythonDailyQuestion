def caesar_password_transform(flag):
    caesar_list = []
    caesar_list_input = input("please input:")
    for letter in caesar_list_input:
        letter_int = ord(letter) - 64
        if 1 <= letter_int <= 26:
            if flag:
                caesar_letter_num = (letter_int + 3) % 26
                if caesar_letter_num == 0:
                    caesar_letter_num = 26
            elif flag == False:
                caesar_letter_num = (letter_int - 3) % 26
                if caesar_letter_num == 0:
                    caesar_letter_num = 26
            caesar_letter = chr(caesar_letter_num + 64)
            caesar_list.append(caesar_letter)
        else:
            continue

    caesar_list = [str(letter) for letter in caesar_list]
    print(" ".join(caesar_list))


if __name__ == '__main__':
    while True:
        print("*****请选择********")
        print("1.凯撒密码--加密")
        print("2.凯撒密码--解密")
        print("3.退出")
        choice_user = input("请输入所需功能的序号：")
        if choice_user.isdigit():
            choice_user = int(choice_user)
            if choice_user == 1:
                flag = True
                caesar_password_transform(flag)
            elif choice_user == 2:
                flag = False
                caesar_password_transform(flag)
            elif choice_user == 3:
                exit("谢谢您的使用O(∩_∩)O")
                # break
            else:
                print("无此序号，请重新选择")
        else:
            print("输入有误，请重新选择")