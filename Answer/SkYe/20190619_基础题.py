strings = input(">>>")
dict_1 = {}
for string in strings:
    dict_1[string] = dict_1.get(string, 0) + 1
print(dict_1)
