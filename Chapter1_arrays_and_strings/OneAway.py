'''
pale, ple -> true
pale, pales -> true
pale, bale -> true
pale, bake -> false

rules:
  insert a ch: len(s2) = len(s1) + 1
  remove a ch: len(s2) = len(s1) - 1
  replace a ch: len(s2) = len(s1)

'''

def one_edit(s1, s2):

  if len(s2) > len(s1)+1 or len(s2) < len(s1)-1:
    return False

  same_length = True if len(s1) == len(s2) else False

  max_s, min_s = (s2, s1) if len(s2) > len(s1) else (s1, s2)

  count = 0
  i = 0
  j = 0  


  while i < len(max_s) and j < len(min_s):
    if max_s[i] != min_s[j]:
      count += 1
      if count > 1:
        return False
      if same_length:
        j += 1
    else:
      j += 1
    i += 1
  return True

s1 = 'pale'
s2 = 'pale'

print(one_edit(s1, s2))
        


  
