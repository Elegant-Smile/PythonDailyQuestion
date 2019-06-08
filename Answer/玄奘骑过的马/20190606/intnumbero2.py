# _*_coding:utf-8 _*_
# Author:Oldyuan
# ChangeTime: 2019/6/6 10:36
# FileName: intnumbero2.py


def intNumeber():
    num = [1,'ww',+100, -1E-16]
    num2 = []
    for i in num:
        isi = isinstance(i,int)
        isi2 = isinstance(i,float)
        if isi == True or isi2 == True :
            num2.append(i)
    print(num2)

def is_Number(s):
    try:
        num = float(s)
        return True
    except:
        return False




if __name__ == "__main__":
    intNumeber()
    is_Number()




