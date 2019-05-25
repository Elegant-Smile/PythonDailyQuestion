import math


def hypotenuse(a, b):
    '''

    :param a: 直角边
    :param b: 直角边
    :return: 斜边长
    '''
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    a = int(input("请输入一条直角边:"))
    b = int(input("请输入另一条直角边:"))
    print("The right triangle third side's length is", hypotenuse(a, b))
