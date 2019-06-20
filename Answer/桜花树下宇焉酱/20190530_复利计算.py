'''
基础题：
设计一个复利计算函数invest（）
它包含三个参数：amount（资金），rate（年利率），time（投资时间）。
键盘输入每个参数后，输出结果：返回每一年的资金总额
比如，amount = 10000 , rate = 8% ,time = 5
'''
def invest():
    amount = int(input('input your amount:'))
    rate = float(input('rate is:'))
    time = int(input('your cycle is:'))
    for i in range(1,time+1):
    	amount *= (1+rate)
    	print('第{}年 : {}'.format(i,amount))	 
    # return amount*(1+rate)**time
    
if __name__ == "__main__":
	invest()