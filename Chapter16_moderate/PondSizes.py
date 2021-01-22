'''
You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally or diagonally. The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.
'''

from collections import defaultdict


def check_value(m, i, j): 
  
  a = 0
  b = 0
  c = 0
  d = 0

  if j > 0:
    a = m[i][j-1]
    m[i][j-1] = 0
    if i > 0:
      b = m[i-1][j-1]
      m[i-1][j-1] = 0
  if i > 0:
    c = m[i-1][j]
    m[i-1][j] = 0
    if j < len(m)-1:
      d = m[i-1][j+1]
      m[i-1][j+1] = 0
   
  m[i][j] = a + b + c + d + 1

  return m

def pond_sizes(m):

  ponds = []

  for i in range (0, len(m)):
    for j in range(0, len(m[i])):
      if m[i][j] != 0:
        m[i][j] = 0
      else: # check (i, j-1), (i-1, j-1), (i-1, j), (i-1, j+1)
        m = check_value(m, i, j)
  for line in m:
    for el in line:
      if el != 0:
        ponds.append(el)
	
  return ponds

m = [ 
[0, 2, 1, 0],
[0, 0, 4, 1],
[1, 1, 0, 1],
[0, 1, 0, 1]
] 



print(pond_sizes(m))


