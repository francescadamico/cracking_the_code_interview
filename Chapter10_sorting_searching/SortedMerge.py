'''
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a methid to merge B into A in sorted order.
'''

def sorted_merge(A, B):

  help_A = []
  new_A = []
  help_A[ : len(A)] = A
  help_A[len(A) : len(A) + len(B)] = B  

  left = 0
  right = len(A)
  current = 0

  while left < len(A) and right < len(A) + len(B):
    if help_A[left] <= help_A[right]:
      new_A.append(help_A[left])      
      left += 1   
    else: # help_A[left] > help_A[right]
      new_A.append(help_A[right])
      right += 1 
    current += 1
    print(current)
  
  for i in range(left, len(A)):
    new_A.append(help_A[i])
  for j in range(right, len(A) + len(B)):
    new_A.append(help_A[j])

  return new_A 

A = [3, 4, 5, 7, 9, 10]
B = [2, 4, 15]

print(sorted_merge(A,B))
