'''
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.
'''


def check_diff(A, B):
  
  ix_A = 0
  ix_B = 0

  small_diff = abs(A[0] - B[0]) # 7, 6, 5, 3
  
  while ix_A < len(A) and ix_B < len(B):    
    diff = abs(A[ix_A] - B[ix_B])
    if diff < small_diff:
        small_diff = diff
    if A[ix_A] <= B[ix_B]:
      ix_A += 1
    else:
      ix_B += 1
  
  return small_diff

def smallest_diff(A, B):

  sort_A = sorted(A) 
  sort_B = sorted(B)

  return check_diff(sort_A, sort_B)



A = [1, 3, 15, 11, 2] # [1, 2, 3, 11, 15]
B = [23, 127, 235, 19, 8] # [8, 19, 23, 127, 235]

print(smallest_diff(A, B))
