raw_string = input(">>")
num = int(input(">>"))
replace_string = input(">>")
print("{}{}{}".format(raw_string[:num], replace_string, raw_string[num + 1:]))
# 更多方法拓展https://blog.csdn.net/saltriver/article/details/52194921
