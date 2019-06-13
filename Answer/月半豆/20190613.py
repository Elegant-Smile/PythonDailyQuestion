#!/bin/env python3

a =[1, 2, 3, 2, 2, 2, 5, 4, 2]
for t in list(set(a)):
	if a.count(t) > len(a)/2 :
		print(t)
