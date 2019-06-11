def jump(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return jump(n-1)+jump(n-2)
    
if __name__ == '__main__':
  assert jump(1)==1
  assert jump(2)==2
  assert jump(3)==3
  assert jump(4)==5
