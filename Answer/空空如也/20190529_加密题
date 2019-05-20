'''
Enter data to be encryted: 2345
Encrypted number: 0987
'''

__author__ = 'Xixin He'
__email__ = 'xixin.he@gmail.com'

number = input('Enter data to be encryted: ')
basic_element = list(range(10))
dictionary = dict(zip(basic_element, basic_element[5:] + basic_element[:5]))

encrypted_number = [str(dictionary[int(digit)]) for digit in number]

encrypted_number[0],encrypted_number[3], encrypted_number[1],encrypted_number[2] = \
encrypted_number[3],encrypted_number[0], encrypted_number[2],encrypted_number[1]

encrypted_number = ''.join(encrypted_number)
print(f'Encrypted number: {encrypted_number}')
