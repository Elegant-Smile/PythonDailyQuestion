rest = 4
while True:
    flag = 1
    sum = rest
    for i in range(5):
        if sum % 4 != 0:
            flag = 0
            break
        sum = sum * 5.0 / 4 + 1
    if flag == 1:
        break
    else:
        rest += 4
print(f'最少有{int(sum)}个')
