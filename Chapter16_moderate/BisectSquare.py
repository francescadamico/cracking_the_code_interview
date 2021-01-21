'''
Given two squares on a two-dimentional plane, find a line that would cut these two squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis. 
'''


def find_center(S):
  
  cx, cy = (S[1][0] - S[0][0])/2 + S[0][0], (S[1][1] - S[0][1])/2 + S[0][1] 
  return cx, cy

def line_through(x1, y1, x2, y2):
  
  c = (x1 * y2 - x2 * y1) / (x1 - x2)
  m = (y1 - c) / x1  

  return m, c
  

def bisect_square(S1, S2):

  c1x, c1y = find_center(S1)
  c2x, c2y = find_center(S2)

  return line_through(c1x, c1y, c2x, c2y)  
  
S1 = [(1, 1), (3, 3)]
S2 = [(4, 3), (9, 8)]

print(bisect_square(S1, S2))



