"""
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬‬

第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。
"""

edge = eval(input("请输入最后一行星星数量(奇数)："))
for i in range(edge):
    if (i + 1) % 2 == 1:
        triangle = '*' * (i + 1)
        triangle = str(triangle)
        print(triangle.center(edge, " "))
