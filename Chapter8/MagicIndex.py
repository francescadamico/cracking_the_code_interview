'''
A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
Follow up: what if the values are not distinct?
'''

'''
Brute force
'''
def magic_index_bf(A):
  for i in range(0, len(A)):
    if A[i] == i:
      return i

'''
Binary search
'''
def magic_index_bs(A, start_ix = 0):
  if len(A) == 0:
    return None
  middle = int(len(A)/2) 
  if A[middle] == middle + start_ix:
    return middle + start_ix
  if A[middle] > middle + start_ix and A[middle+1] != A[middle]:
      return magic_index_bs(A[:middle], start_ix)
  else: # A[middle] < middle
    return magic_index_bs(A[middle+1:], start_ix + middle+1)

A = [-19, -13, -5, 0, 1, 5, 7]

print(magic_index_bs(A))

