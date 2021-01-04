def merge_sort(A):
  help_A = []
  return merge_sort_int(A, help_A, 0, len(A)-1)

def merge_sort_int(A, help_A, low, high):
  if low < high:   
    middle = low + int((high-low)/2)
    merge_sort_int(A, help_A, low, middle)
    merge_sort_int(A, help_A, middle+1, high)
    merge(A, help_A, low, middle, high)
  return A

def merge(A, help_A, low, middle, high):
  help_A[low : high+1] = A[low : high+1]  
  
  help_left = low
  help_right = middle+1
  current = low

  while help_left <= middle and help_right <= high:
    if help_A[help_left] <= help_A[help_right]:
      A[current] = help_A[help_left]
      help_left += 1
    else: # help_A[help_right] < help_A[help_left]
      A[current] = help_A[help_right]
      help_right += 1
    current += 1

  rest = middle - help_left
  for i in range(rest + 1):
    A[current + i] = help_A[help_left + i]
    print(A[current + i])
  return A 

to_sort = [5, 7, 3, 9, 9, 10, 4]
sort = merge_sort(to_sort)
print('sort = ', str(sort))  
