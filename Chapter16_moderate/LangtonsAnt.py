
'''
An ant is sitting on an infinite grid of white and black squares. Initially, the grid is all white and the ant faces right. At each step, it does the following:
(1) at a white square, flip the color of the square, turn 90 degrees rigth (clockwise), and move forward one unit.
(2) at a black square, flip the color of the square, turn 90 degrees left (counter-clockwise), and move forward one unit.

Write a program to simulate the firs K moves that the ant makes and orint the final board as a grid. Note that you are not provided with the data structure to represent the grid. THis is something you must design yourself. The only input to your method is K. YOu should print the final grid and return nothing.
'''

def change_dir_move(direct, clk, i, j):
	
  if clk == True:
    direct += 1
  else:
    direct -= 1
 
  if direct > 3:
    direct = direct % 4
	
  dir_list = {
                0: (i, j+1),
                1: (i+1, j),
                2: (i, j-1),
                3: (i-1, j)
             } 	# [right, down, left, up]
	
  return dir_list[direct]	# new (i,j)	

def grid_to_string(grid):

  min_row = min_col = max_row = max_col = 0
	
  for el in grid:
    if el[0] < min_row:
      min_row = el[0]
    elif el[0] > max_row:
      max_row = el[0]
    if el[1] < min_col:
      min_col = el[1]
    elif el[1] > max_col:
      max_col = el[1]
	
  for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
     
      if (i,j) in grid:        
        print('X', end = "")
      else:
        print('_', end = "")
    
    print('\n', end = "")


def print_k_moves(k): # 5

  grid = set()
  (i, j) = (0, 0)

  for d in range(0, k):
    if (i, j) not in grid:	# white 
      grid.add((i, j))
      (i, j) = change_dir_move(d, True, i, j)
    else: 			# black
      grid.remove((i, j))
      (i, j) = change_dir_move(d, False, i, j)

  grid_to_string(grid)


print_k_moves(30)
