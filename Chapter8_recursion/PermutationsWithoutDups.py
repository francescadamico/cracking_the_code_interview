import math

def perm(string):

  p_list = []
  	
  length = len(string)
  
  if length <= 1:
    p_list = [string]
    return p_list
	
  ch = string[0]

  p_list = perm(string[1:])

  temp_p = [[0 for i in range(length)] for j in range(math.factorial(length))]

  point = 0  
  while point < length:
    for i in range(len(p_list)):

      temp_p[(length-1)*point+i][:point] = p_list[i][:point]
      temp_p[(length-1)*point+i][point] = ch
      temp_p[(length-1)*point+i][point+1:] = p_list[i][point:]
      
    point += 1
	
  return temp_p

a = 'fra'

permy = perm(a)

for i in permy:
  print(''.join(i)), 


