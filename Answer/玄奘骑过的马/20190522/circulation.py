# -*- coding: utf-8 -*-
#Author:Oldyuan

def circulation(peopleNumber):
    lic = list(range(1, peopleNumber+1))
    count = 0
    while len(lic) >1:
        lico = lic[:]
        print(lico)
        for i in range(0, len(lico)):
            count = count+1

            if count %3 == 0:
                lic.remove(lico[i])
    print(lic)




if __name__ =="__main__":
    peopleNumber = input('请输入有多少人：')
    circulation(peopleNumber)



