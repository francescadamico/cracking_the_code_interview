

from collections import defaultdict

def master_mind(solution, test):

  sol_dict = defaultdict(int)
  test_dict = defaultdict(int)
  hits = 0
  pseudo_hits = 0

  for i in range(len(test)):
    if test[i] == solution[i]:
      hits += 1 # hits = 2
    else:
      test_dict[test[i]] += 1 # test_dict = {'G' : 3, 'B' : 1}
      sol_dict[solution[i]] += 1 # sol_dict = {'Y' : 1, 'R' : 1, 'G': 1, 'B' : 1}
    
  for k in test_dict:
    if k in sol_dict:
      pseudo_hits += min(test_dict[k], sol_dict[k]) # pseudo_hits = 1

  return hits, pseudo_hits

sol = 'RYBG'
test = 'RYBG'

print(master_mind(sol, test))

