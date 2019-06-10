amount = int(input("请输入金额："))
rate = float(input("请输入年利率："))
time = int(input("请输入投资时间（年）："))
def invest(amount,rate,time):
  for i in range(time):
    money_every = amount * pow((1+rate),i)
    print("第{0}年的资金总额为：{1}" .format(i,money_every))
    
invest(amount,rate,time)
