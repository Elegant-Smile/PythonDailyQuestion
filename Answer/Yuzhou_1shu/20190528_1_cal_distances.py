from math import sqrt, pow


def cal_distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


if __name__ == '__main__':
    x1, y1, x2, y2 = input("请输入坐标数字:").split()
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    print(cal_distance(x1, y1, x2, y2))
