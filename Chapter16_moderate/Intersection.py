'''
Given two straight line segments (represented as a start and an end point), compute the point of intersection. if any.
'''

'''
the class segment does not have a solution for the segments that are parallel to the y-axis
'''
class segment:
  
  def __init__(self, start_pt, end_pt):
    self.start = start_pt
    self.end = end_pt
    self.slope = (end_pt[1] - start_pt[1]) / ((end_pt[0] - start_pt[0])) if start_pt[0] != end_pt[0] else 0
    self.y_intersec = start_pt[1] - self.slope * start_pt[0] 

def intersection_parallel(seg1, seg2):

  if seg1.y_intersec != seg2.y_intersec: # the segments belong to parallel lines
    return None
  else:
    # check if common points
    if any([all([seg1.start[0] < seg2.start[0], seg2.start[0] > seg1.end[0]]), all([seg2.start[0]< seg1.start[0], seg1.start[0]> seg2.end[0]])]):
      return None    
    if seg1.start[0] <= seg2.start[0]:
      return seg2.start
    else:
      return seg1.start

def intersection(seg1, seg2):

  if seg1.slope == seg2.slope:
    return intersection_parallel(seg1, seg2)  
  else:
    # find point of intersection between the lines
    x_int = (seg2.y_intersec - seg1.y_intersec) / (seg1.slope - seg2.slope)
    y_int = seg1.slope * x_int + seg1.y_intersec

    # check if point of intersection belongs to seg1 and seg2
    if any([x_int < seg1.start[0], x_int > seg1.end[0], y_int < seg1.start[1], y_int > seg1.end[1], x_int < seg2.start[0], x_int > seg2.end[0], y_int < seg2.start[1], y_int > seg2.end[1]]):
      return None
    return [x_int, y_int]  

     

# [start_x, start_y, end_x, end_y]
a = segment([2, 0], [5, 3])
b = segment([5, 2], [7, 2])

print(intersection(a, b))




