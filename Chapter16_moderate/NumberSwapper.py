'''
Write a function to swap two numbers in place (that is, without temporary variables)
'''

def swap_nums(a,b):

  a = (a * 10**(len(str(b))) + b) 
  b = a // 10**(len(str(b)))  
  a = a % 10**(len(str(a))-len(str(b)))
  
  return a, b
  


print(swap_nums(13,537856873))

