#!/bin/env python3

while(1):
	print("Please enter an odd number: ", end='')
	a = int(input())
	if a % 2 != 1:
		print("number (" + str(a) + ") is not an odd number")
	else:
		i=0
		lines = round(a/2)+1
		print(lines)
		while(i<lines):
			whiteSpace = int(a/2) - i
			t = 0
			while(t < whiteSpace):
				print (' ', end='')
				t+=1
			stars = a - 2 * whiteSpace
			t = 0
			while(t < stars):
				print('*', end='')
				t+=1
			t = 0
			while(t < whiteSpace):
				print (' ', end='')
				t+=1
			print('\n')
			i+=1
		exit()

