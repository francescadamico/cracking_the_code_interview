
def merge(arr, L, R):
  
  i = j = k = 0

  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1
  
  while j < len(R): 
    arr[k] = R[j]
    j += 1
    k += 1

  return arr


def merge_sort(arr):
  
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
 
    merge_sort(L)
    merge_sort(R) 
    merge(arr, L, R)
  return arr

A = [3, 10, 1, 6, 4, 3, 2]
print(merge_sort(A))
