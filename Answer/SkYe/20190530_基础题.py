def invest(amount,rate,time):
	for _ in range(time):
		amount *= 1+rate
	return amount
def main():
	amount=eval(input('输入本金:'))
	rate=eval(input('输入年利率:'))
	time=eval(input('投资年限:'))
	print(invest(amount,rate,time))
main()