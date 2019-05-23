def soccer_team():
    """
    一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
    编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
    然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
    """

    count = 1  # 记录询问次数
    sum = 0  # 统计符合总人数

    for item in range(1, 11):
        print('第%d次询问' % count)
        sex = input('请输入性别(m表示男性，f表示女性):')
        age = int(input('请输入你的年龄：'))
        if sex == 'm' or 10 > age > 12:
            print('抱歉，你不符合我们的条件，我们需要10岁到12岁的女孩')
        elif sex == 'f' and age > 12 or age < 10:
            print('你的年龄不符合我们的要求哦')
        elif sex == 'f' and 10 <= age <= 12:
            print('恭喜你加入我们的足球队！')
            sum += 1
        print("\n")
        count += 1
    print('询问10个人后，目前我们一共有%d人加入' % sum)


soccer_team()
