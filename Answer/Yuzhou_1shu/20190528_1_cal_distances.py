from math import sqrt, pow


def cal_distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


if __name__ == '__main__':
    x1, y1, x2, y2 = map(float, input("请输入坐标数字:").split())
    print(cal_distance(x1, y1, x2, y2))
