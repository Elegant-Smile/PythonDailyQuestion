'''
row 1:  [1]
row 2:  [1, 1]
row 3:  [1, 2, 1]
row 4:  [1, 3, 3, 1]
row 5:  [1, 4, 6, 4, 1]
row 6:  [1, 5, 10, 10, 5, 1]
row 7:  [1, 6, 15, 20, 15, 6, 1]
row 8:  [1, 7, 21, 35, 35, 21, 7, 1]
row 9:  [1, 8, 28, 56, 70, 56, 28, 8, 1]
row 10:  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

'''

__author__ = 'Xixin He'
__email__ = 'xixin.he@gmail.com'


import numpy as np

def get_triangle():
  row= np.array([1])
  yield row
  margin_array = np.array([0])
  while True:
    next_row = np.concatenate((margin_array, row)) + np.concatenate((row, margin_array))
    yield list(next_row)
    row = next_row

triangle = get_triangle()
for i in range(10):
  print(f"row {i+1}: ", triangle.__next__())
