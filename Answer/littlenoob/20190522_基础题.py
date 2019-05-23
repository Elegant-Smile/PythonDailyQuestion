n = input('请输入人数')
circle = list(range(1,int(n) + 1))
i = 0
count = 1
while len(circle) > 1:
    if count == 3:
        print(f'{circle[i]}出队')
        del(circle[i])
        count = 1
    i = (i + 1) % len(circle)
    count += 1
print(f'最后出队的是{circle[0]}')
