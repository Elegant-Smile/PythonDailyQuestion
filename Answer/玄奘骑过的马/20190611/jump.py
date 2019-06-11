# _*_coding:utf-8 _*_
# Author:Oldyuan
# ChangeTime: 2019/6/11 17:57
# FileName: jump.py



def jumps(n):
    if n ==1:
        return 1
    if n==2:
        return 2
    return jumps(n-1)+jumps(n-2)


if __name__ == "__main__":
    print(jumps(4))


