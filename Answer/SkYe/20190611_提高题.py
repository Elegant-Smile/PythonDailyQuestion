'''
1.青蛙🐸的每一次起跳都有两个选择（一阶or两阶），每次起跳就会产生类似二叉树的两个树枝
2.当n=1时，有一种跳法----↓
  当n=2时，有两种跳法----→当n<=3时，跳法数等于n
  当n=3时，有三种跳法----↑
3.总跳法数等于二叉树的叶子结点个数
'''


def jump(steps):
    if steps <= 3:
        return steps
    return jump(steps - 1) + jump(steps - 2)


if __name__ == '__main__':
    steps = int(input("总台阶数:"))
    print('一共有{}种跳法'.format(jump(steps)))
