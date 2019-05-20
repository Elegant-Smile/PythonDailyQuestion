__author__ = "Yuzhou_1shu"


def company_encrytion(number):
    # 1、解数字的每一位数
    a = number % 10         # 个位数
    aa = number // 10 % 10   # 十位数
    aaa = number // 100 % 10 # 百位数
    aaaa = number // 1000    # 千位数

    # 2、加上5
    a = (a + 5) % 10
    aa = (aa + 5) % 10
    aaa = (aaa + 5) % 10
    aaaa = (aaaa + 5) % 10

    # 3、交换
    a, aaaa = aaaa, a
    aa, aaa = aaa, aa
    # number = str(aaaa) + str(aaa) + str(aa) + str(a)
    number = aaaa*1000 + aaa*100 + aa*10 + a

    print("加密后的数字: ", number)


if __name__ == "__main__":
    number = int(input("请输入一个四位数："))
    print("加密前的数字：", number)
    company_encrytion(number)