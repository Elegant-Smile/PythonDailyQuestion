#a0,a1,b0,b1，求（a0,b0)和(a1,b1)的距离
def two_point_distance(a,b,c,d):
    e = ((a-c)**2+(b-d)**2)**0.5
    print("坐标(%d,%d)和(%d,%d)之间的距离是 %.1f"%(a,b,c,d,e))

if __name__ == '__main__':
    a,b,c,d = map(float,input("请依次输入四个数字:").split())
    two_point_distance(a,b,c,d)
