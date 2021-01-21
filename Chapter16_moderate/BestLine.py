'''
Given a two-dimentional graph with points on it, find a line which passes the most number of points.


y = mx + c
m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1
'''


from collections import defaultdict


def find_line(p1, p2):
  
  x1, y1 = p1[0], p1[1]
  x2, y2 = p2[0], p2[1]
  
  m = (y2 - y1) / (x2 - x1)
  c = y1 - m * x1

  return m, c

def best_line(points):

  lines = defaultdict(int)
  i = 0
  max_line = 0, 0
  
  while i < len(points) - 1:
    for np in points[i+1 : ]:
      m, c = find_line(points[i], np)
      lines[m, c] += 1
      if lines[m, c] > lines[max_line]:
        max_line = m, c
    i += 1 
  
  return max_line


p1 = (6, 6)
p2 = (4, 4)
p3 = (11, 11)
p4 = (3, 5)
p5 = (1, 3)
p6 = (2, 4)
p7 = (5, 7)
p8 = (11, 13)

points = [p4, p1, p3, p2, p5, p6, p7]



print(best_line(points))
