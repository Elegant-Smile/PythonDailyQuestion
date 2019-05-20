'''
solution 1
a vs z
b vs x
c vs y
'''

__author__ = 'xixin he'
__email__ = 'xixin.he@gmail.com'

from itertools import permutations

team_a = ['a', 'b', 'c']
team_b = ['x', 'y', 'z']

possible_match_lists = []

for possible_team_b_sequence in list(permutations(team_b)):
  possible_match_lists.append(dict(zip(team_a, possible_team_b_sequence)))
  
final_match_lists = list(filter(lambda x: x['a'] != 'x' and \
                          x['c'] != 'x' and \
                          x['c'] != 'z', possible_match_lists))

for index, match_list in enumerate(final_match_lists):
  print(f'solution {index+1}')
  for competitors in match_list.items():
    print(' vs '.join(competitors))