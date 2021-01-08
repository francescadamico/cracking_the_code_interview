'''
Given two straight line segments (represented as a start and an end point), compute the point of intersection. if any.
'''
class segment:
  def __init__(self, start_pt, end_pt):
    self.start = start_pt
    self.end = end_pt
    self.slope = (end_pt[1] - start_pt[1]) / ((end_pt[0] - start_pt[0])) if start_pt[0] != end_pt[0] else 0
    self.y_intersec = start_pt[1] - self.slope * start_pt[0] 


def Intersection(seg1, seg2):

  # find point of intersection between the lines
  x_int = (seg2.y_intersec - seg1.y_intersec) / (seg1.slope - seg2.slope)
  y_int = seg1.slope * x_int + seg1.y_intersec

  # check if point of intersection belongs to seg1 and seg2
  if any([x_int < seg1.start[0], x_int > seg1.end[0], y_int < seg1.start[1], y_int > seg1.end[1], x_int < seg2.start[0], x_int > seg2.end[0], y_int < seg2.start[1], y_int > seg2.end[1]]):
    return None

  # what if the segments are coincident/belong to the same line?
  
  return x_int, y_int  

     

# [start_x, start_y, end_x, end_y]
a = segment([3, 1], [5, 4])
b = segment([1, 2], [7, 2])

print(b.start, b.end, b.slope, b.y_intersec)
print(Intersection(a, b))




