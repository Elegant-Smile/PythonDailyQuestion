# coding=utf-8

# Coordinate: left top corner is coordinate (0, 0), right bottom corner is (lines -1, lines - 1)
# Direction:  up (0, -1), down (0, 1), right (1, 0), left (-1, 0)

__author__ = 'xixin he'
__email__ = 'xixin.he@gmail.com'

def get_next_direction(direction):
  up = {'x': 0, 'y': -1}
  down = {'x': 0, 'y': 1}
  left = {'x': -1, 'y': 0}
  right = {'x': 1, 'y': 0}
  still = {'x': 0, 'y': 0}
  if direction == down:
    next_direction = right
    
  elif direction == right:
    next_direction = up
    
  elif direction == up:
    next_direction = left
    
  elif direction == left:
    next_direction = down
    
  else:
    next_direction = still
  return next_direction

def get_box(lines):
  
  coordinate = {'x':0, 'y':0}
  direction = {'x': 0, 'y': 1}
  
  box = [['' for i in range(lines)] for i in range(lines)]
  for i in range(lines ** 2):
    box[coordinate['y']][coordinate['x']] = f'{str(i+1):0>2}'
    next_coordinate = {'x': coordinate['x'] + direction['x'] ,'y': coordinate['y'] + direction['y'] }
    
    if next_coordinate['x'] < 0 \
    or next_coordinate['x'] >= lines\
    or next_coordinate['y'] < 0 \
    or next_coordinate['y'] >= lines \
    or box[next_coordinate['y']][next_coordinate['x']] != '' :
      direction = get_next_direction(direction)
      next_coordinate = {'x': coordinate['x'] + direction['x'] ,'y': coordinate['y'] + direction['y'] }
      
    coordinate = next_coordinate
  return box

box = get_box(5)

print('\n'.join([' '.join(line) for line in box]))
