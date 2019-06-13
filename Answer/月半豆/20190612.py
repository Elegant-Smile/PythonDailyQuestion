#!/bin/env python3


a =[1, 2, 3, 2, 2, 2, 5, 4, 2]
odd = []
even = []
for t in a:
	if t % 2 == 0:
		even.append(t)
	else:
		odd.append(t)

print(odd+even)
