'''
2561327494111820313
'''

__author__ = 'xixin he'
__email__ = 'xixin.he@gmail.com'

def factorial(number):
  start = 1
  fact = 1
  while start <= number:
    yield fact
    start += 1
    fact *= start

fact = factorial(20)
sum = 0

for i in fact:
  sum += i
  
print(sum)