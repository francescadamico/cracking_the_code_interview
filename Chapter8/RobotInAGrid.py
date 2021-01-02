'''
Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right
'''


def go_left(maze):  
  if len(maze[0]) > 1:  
    return maze[-1][-2]  

def go_up(maze):  
  if len(maze) > 1:
    return maze[-2][-1]

def left_or_up(maze, steps):
  left = go_left(maze)
  if left == 'o':
    steps.append('left')
    # eliminate column
    [row.pop(-1) for row in maze]   
    return maze 
  up = go_up(maze)     
  if up == 'o':
    steps.append('up')
    # eliminate row
    del maze[-1]
    return maze
  return False



def get_out(maze, steps):
  if len(maze) <= 1 and len(maze[0]) <= 1:
    return steps
  else: 
    new_maze = left_or_up(maze, steps)
    if new_maze == False:
      return 0
    else:
      return get_out(new_maze, steps)

steps = []

test_maze = [
             ['o', 'o', 'o', 'o', 'o', 'o'],
             ['o', 'o', 'o', 'o', 'X', 'o'],
             ['o', 'X', 'o', 'o', 'o', 'o'],
             ['o', 'X', 'o', 'X', 'o', 'o']
            ]
#test_maze[4] = ['o', 'o', 'o', 'o', 'o', 'o']
#test_maze[5] = ['o', 'o', 'o', 'o', 'o', 'o'] 

steps = get_out(test_maze, steps)

new_steps = steps.copy()
for i in range(len(steps)):
  print(steps[i])
  new_steps[len(steps) -1 - i] = 'right' if steps[i] == 'left' else 'down'
print(new_steps)

