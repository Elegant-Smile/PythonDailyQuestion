#求1到20的数乘的和
result = 0
for i in range(1,21):
    num = 1
    for j in range(1,i+1):
        num *= j
    result += num
print(result)