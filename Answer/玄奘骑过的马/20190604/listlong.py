
# -*- coding: utf-8 -*-
#Author:Oldyuan

'''
def doKnow():
    A=[11, 22, 33, 44, 55]
    for i in A:
        print(i,'-------')
        for j in range(len(A)):
            if i == A[j]:
                break
            else:
                s = A[j]*A[j-1]
                print(s)

'''

def donKnow():
    A = [10, 20, 30, 40, 50]
    for i in A:
        B = A.copy()
        for j in range(len(B)):
            if i == B[j]:
                del B[j]
                print(B)
                s = 1
                for k in range(len(B)):
                    s = s*B[k]
                print(s)
                break

        print(j,'------')


if __name__ =="__main__":
    donKnow()
