# -*- coding: utf8 -*-
#Author:Oldyuan


def selectPlayer():
    containt = []
    for i in range(10):
        name = raw_input('输入姓名：')
        age = input('输入一下年龄：')
        genders = raw_input('输入一下性别m表示男性，f表示女性')
        print(type(genders))

        if age >= 10 & age <=12 :
            if genders == 'm':
                containt.append(name)

    print("his name ：",containt,"number：",len(containt))


if __name__ =="__main__":
    selectPlayer()





