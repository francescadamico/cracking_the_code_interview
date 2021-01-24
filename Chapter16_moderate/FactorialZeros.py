'''
Write an algorithm which computes the number of trailing zeros in n factorial.
'''
import math 


def factorial_zeros(n):
  """ This algorithm give the same result for 
  5**i and 5**(i+1)-1
  Maybe that's not correct: you lose something
  """

  k = int(math.log(n, 5))
  trail_zeros = 0

  for i in range(1, k+1):
    trail_zeros += n // 5**i

  return trail_zeros


num = 126
print(factorial_zeros(num))
