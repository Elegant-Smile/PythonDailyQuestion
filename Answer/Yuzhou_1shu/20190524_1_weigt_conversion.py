def weight_conversion(weight, option):
    if option == '1':
        return str(weight * 1000) + 'g'
    elif option == '2':
        return str(weight / 1000) + 'kg'
    else:
        print('没有此选项')


if __name__ == '__main__':
    option = input('1. kg to g\n2. g to kg\n请选择:')
    weight = int(input('请输入重量:'))
    print(weight_conversion(weight, option))
