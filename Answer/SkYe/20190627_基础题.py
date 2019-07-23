import numpy as np


def fn(n):
    """
    .arange()生成数列（一维）
    .reshape(n,n)将数据整理为n*n的矩阵
    """
    a = np.arange(n * n).reshape(n, n)
    print(a)
    print(a.T)  # 转置矩阵
    b = ''
    for i in a.T:
        for j in i:
            j = str(j)
            b += ''.join(j) + ' '
        b = b + '\n'
    print(b)


n = int(input("行列："))
fn(n)
