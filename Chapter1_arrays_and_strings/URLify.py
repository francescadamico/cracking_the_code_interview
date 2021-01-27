'''

'Mr John Smith    ', 13
'Mr John Smith    '
'Mr%20John Smith    '   
'Mr%20John%20Smith'

'''


def URLify(s, len_s):

  i = 0

  while i < len_s:
    if s[i] == ' ': 
      j = i + 3      
      s[j:]= s[i+1:len_s] 
      s[i:i+3]= '%20'
      i += 2
      len_s += 2
    i += 1
  
  return s


s, len_s = 'Mr John Smith    ', 13

s_list = list(s)

print(URLify(s_list, len_s))
