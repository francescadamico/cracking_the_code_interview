'''
Write a method to return all subsets of a set.
'''
def power_set(s):    
  
  subsets = []
   
  el = s.pop()	
  print(el)	

  if len(s) > 0:

    subsets += power_set(s) 

    sub_plus = []

    for i in subsets:
      sub_plus += [i.copy()]
      i.add(el)

    subsets += sub_plus

  subsets += [{el}]			

  return subsets

a = {3,6,1,7}
print(power_set(a))
