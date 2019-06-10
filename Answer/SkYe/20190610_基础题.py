strings = input("请输入需要加密的内容：")
encrypted_strings = []
for string in strings:
    if string == chr(32):
        encrypted_strings.append(string)  # 空格不加密
    else:
        ascii_num = ord(string) - 64 + 3
        if ascii_num == 26:
            encrypted_strings.append(chr(26 + 64))
        else:
            encrypted_strings.append(chr(ascii_num % 26 + 64))
print('{}'.format(''.join(encrypted_strings)))
