'''
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's deoendencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
'''

def create_dict(p, p_dep):
  
  p_dict = {}
  for k in p:
    p_dict[k] = []
    for (i, j) in p_dep:
      if j == k:              
        p_dict[k].append(i)

  return p_dict

def pop_proj_dep(p_dict, ordered_list):

  for k in p_dict:
    for i in p_dict[k]:
      if i in ordered_list:
        p_dict[k].remove(i)

  return p_dict

def create_order(p_dict, ordered_list = []):
  
  temp_count = len(ordered_list)

  if len(p_dict) == len(ordered_list):
    return ordered_list
  for k in p_dict:
    if p_dict[k] == []:
      if k not in ordered_list:
        ordered_list.append(k)
  if len(ordered_list) == temp_count:
    return -1
  clean_p_dict = pop_proj_dep(p_dict, ordered_list)  
  return create_order(clean_p_dict, ordered_list)  


def build_order(p, p_dep):
  
  p_dict = create_dict(p, p_dep)
  ordered_list = create_order(p_dict) 
  
  return ordered_list
       

proj = ['a', 'b', 'c', 'd']

proj_dep = [('a', 'd'), ('b', 'c'), ('d', 'b'), ('a', 'b')]

print(build_order(proj, proj_dep))


