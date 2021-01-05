
def binary_search(A, x, low, high):

  if low > high:
    return -1

  mid = low + int((high - low) / 2)

  if x == A[mid]:  
    return mid

  if x < A[mid]:
    return binary_search(A, x, low, mid - 1)
 
  else:
    return binary_search(A, x, mid + 1, high)

test_array = [-100, -14, 4, 5, 120, 210, 354]
find_pos = binary_search(test_array, 120, 0, len(test_array) -1)
print(find_pos)  
