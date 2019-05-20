telephone_num = input("加密前的数据：")
telephone_num_new = []
for number in telephone_num:
    int_num = int(number)
    int_num = (int_num + 5) % 10
    telephone_num_new.append(int_num)

telephone_num_new[0], telephone_num_new[3] = telephone_num_new[3], telephone_num_new[0]
telephone_num_new[1], telephone_num_new[2] = telephone_num_new[2], telephone_num_new[1]

number_str = ""

for number_new in telephone_num_new:
    number_str = number_str + str(number_new)

print("加密后的数据：", number_str)
