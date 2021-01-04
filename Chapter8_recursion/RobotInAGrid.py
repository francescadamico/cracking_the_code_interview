'''
Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right
'''

class Maze:
  def __init__(self, m, row=0, col=0):
    self._inner = m
    self._rows = len(m)
    self._row = row
    self._cols = len(m[0])
    self._col = col
   
  def sub_maze_right(self):
    return Maze(m, row, col + 1)

  def sub_maze_down(self):
    return Maze(m, row + 1, col) 
  
  def get(self, row, col):
    r = row + self._row
    c = col + self._col
    if r >= self._rows || c >= self._cols:
      return "X"
    return self._inner[row + self._row][col + self._col]
  
  def just_one_cell(self):
    return (self._cols - self._col == 1) and (self._rows - self._row == 1)


def solution(maze):
  if maze.just_one_cell():
    return []
  if maze.get(0, 1) != "X":
    s = solution(maze.sub_maze_right())
    if s is not None:
      return ["right"] + s
  if maze.get(1, 0) != "X":
    s = solution(maze.sub_maze_down())
    if s is not None:
      return ["down"] + s
  return None


def go_left(maze):  
  if len(maze[0]) > 1:  
    return maze[-1][-2]  

def go_up(maze):  
  if len(maze) > 1:
    return maze[-2][-1]

"""
WOW: A function that return boolean or maze.... that's crazy.
If you want describe a no return use None.
"""
def left_or_up(maze, steps):
  left = go_left(maze)
  if left == 'o':
    steps.append('left')
    # eliminate column
    """
    WTF!!!!!!
    DON'T USE LIST COMPREHENSION TO WORK LIKE A FOR IN A SIDE EFFECT.
    Use method name instead of comment to describe what you want to do
    """
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
  """Use if guard is better than if else schema."""
  if len(maze) <= 1 and len(maze[0]) <= 1:
    return steps
  new_maze = left_or_up(maze, steps)
  if not new_maze:
    return []
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

