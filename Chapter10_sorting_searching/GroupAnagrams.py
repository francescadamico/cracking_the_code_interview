'''
Write a method to sort an array of strings so that all the anagrams are next to each other
'''
from collections import defaultdict


def anagram(string_a, string_b):

  ch_dict = defaultdict(int)

  if len(string_a) != len(string_b):
    return False
  
  for ch in string_a:
    ch_dict[ch] += 1

  for ck in string_b:
    ch_dict[ck] -= 1

  for k in ch_dict:
    if ch_dict[k] != 0:
      return False
  return True  
  
def anagram_sort(string_a, string_b):
  return sorted(string_a) == sorted(string_b) 

def group_anagram(A):
  i = 0
  while i < len(A):
    ite = 0
    for j in range(i + 1, len(A)):            
      if anagram_sort(A[i], A[j]):
        ite += 1
        A[i + ite], A[j] = A[j], A[i + ite]  
    
    i = i + 1 if ite == 0 else i + ite
  
  return A
        
    

test = ['fra', 'bla', 'etc', 'arf', 'raf', 'lab']

print(group_anagram(test))
print(group_anagram(test) == ['fra', 'arf', 'raf', 'bla', 'lab', 'etc'])


