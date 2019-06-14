""""
求出任意非负整数区间中1出现的次数。

比如，1~13中包含1的数字有1、10、11、12、13，1~13的整数中1出现的次数是6次。
那100~1300的整数中1出现的次数是多少呢？
"""

def num(startnum, endnum):
    numstr = ''

    for i in range(startnum, endnum + 1):
        numstr += str(i)

    print(numstr.count('1'))


if __name__ == '__main__':
    num(100, 1300)
