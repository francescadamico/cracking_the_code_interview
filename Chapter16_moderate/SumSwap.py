'''
Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two arrays the same sum.
'''


from collections import defaultdict

def sum_swap(A, B):
	
  set_B = set()
  sum_A = 0
  sum_B = 0
  B_dict = defaultdict(list)
  for a in A:
    sum_A += a 		# 11
  for b in B:
    sum_B += b		# 15
    set_B.add(b) 

  if (sum_A + sum_B)%2 != 0:	# false
    return -1		

  same_sum = int((sum_A + sum_B)/2)	# 13

  for a in A:
    b = a + same_sum - sum_A	# 6
    if b in set_B:			# true 
      return a, b 		# 4, 6
	
  return -1

A = [6, 1, 1, 1, 1, 2]
B = [5, 0, 8, 3]

print(sum_swap(A, B)) 	
