a = input("please input the list:")
b = [int(i) for i in a.split()]
count = len(b) / 2
flag = False
# 创建字典
dicts = dict.fromkeys(b, 0)
for num in b:
    dicts[num] += 1
print(dicts)
# 对字典排序
dic = sorted(dicts.items(), key=lambda value: value[1])
print(dic)
for key, value in dic:
    if value > count:
        flag = True
        print(key)

if flag == False:
    print(0)
