'''
Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted. Minimize n-m 
'''



def find_min_max(arr, start, end):	# (arr, 6, 7)

  mini = arr[start]		# 7
  maxi = arr[end]		# 12

  for a in arr[start+1:len(arr)]:
    if a < mini:
      mini = a	# 6
	
  for b in arr[0:end]:		
    if b > maxi:
      maxi = b	# 12
	
  return mini, maxi

def find_pos(element, arr, low, high):		# (12, arr, 8, 9)
	
	# arr[low: high] is a sorted array => binary search
  mid = low + (high-low)//2		# 10

  if element == arr[mid] or low == high:
    return mid
  if element > arr[mid]:
    return find_pos(element, arr, mid+1, high)
  else:
    return find_pos(element, arr, low, mid-1) 

def sub_sort(arr):

  for i in range(len(arr)-1):		# (0,12)
    if arr[i+1] < arr[i] :
      start_ix = i+1		# i = 5 -> start_ix = 6
      break

  for j in range(len(arr)-1, 0, -1):	# (12, 0, -1)
    if arr[j-1] > arr[j]:		
      end_ix = j-1		# end_ix = 7
      break

  mini, maxi  = find_min_max(arr, start_ix, end_ix)	# (arr, 6, 7)

  m = find_pos(mini, arr, 0, start_ix-1)		# (6, arr, 0, 5)
  n = find_pos(maxi, arr, end_ix+1, len(arr)-1)	# (12, arr, 8, 12)

  return m,n


A = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]  # len(A) = 13

print(sub_sort(A))  
