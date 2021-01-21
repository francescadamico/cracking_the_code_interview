'''
Yoa are given an array of integers (both positive and negative). Find the contiguous sequence with the largest sum. Return the sum.
'''

# if curr_summ < 0 
# compare prev_summ to max_summ -> if bigger substitute max_summ, max_start, max_end 
# start new curr_summ
# if curr_summ > 0 and < prev_summ
# compare prev_summ to max_summ -> if bigger substitute max_summ, max_start, max_end 
# keep curr_summ
 

def max_sum(A):

  summ = 0

  max_summ = 0
	
  for n in A:
    summ += n
    if summ > max_summ:
      max_summ = summ
    elif summ < 0:
      summ = 0
  
  return max_summ

A = [-1, -3, 2, 4, 1]

print(max_sum(A))

