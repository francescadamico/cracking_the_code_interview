
def quick_sort(A):
  return quick_sort_int(A, 0, len(A)-1)

def quick_sort_int(A, left, right):
  index = partition(A, left, right)
  if left < index - 1: # quick sort left part
    quick_sort_int(A, left, index-1)
  if right > index:
    quick_sort_int(A, index, right)
  return A

def partition(A, left, right):
  pivot = A[left + int((right-left)/2)]
  print(pivot)
  while left <= right:
    while A[left] < pivot:
      left += 1
    while A[right] > pivot:
      right -= 1
    if left <= right:
      A[left], A[right] = A[right], A[left]
      left += 1
      right -= 1
  return left

to_sort = [5, 7, 3, 9, 9, 10, 4]
sort = quick_sort(to_sort)
print('sort = ', str(sort))  
