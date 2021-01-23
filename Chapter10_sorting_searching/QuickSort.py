
def partition(arr, low, high):
  
  i = low - 1
  pi = arr[high]

  for j in range(low, high):
    if arr[j] < pi:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[high] = arr[high], arr[i+1]

  return i+1


def quick_sort(arr, low, high):
  if len(arr) == 1:
    return arr

  if low < high:
  
    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)
  


A = [5, 3, 8, 1, 34, 65]
quick_sort(A, 0, len(A)-1)
print(A)
