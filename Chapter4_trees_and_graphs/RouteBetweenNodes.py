'''
Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E. 
'''

class Node:
  def __init__(self, value):
    self.value = value
    self.adj = []


def DFS(s, e, visited_nodes = None, found = False):
  
  if visited_nodes == None:
    visited_nodes = set()

  if e.value == s.value:
    found = True
    return found

  visited_nodes.add(s)
  for a in s.adj:
    if a not in visited_nodes:
      found = DFS(a, e, visited_nodes, found)
  
  return found

R = Node(1)

T = Node(8)

N1 = Node(2)
N2 = Node(3)
N3 = Node(4)
N4 = Node(5)
N5 = Node(6)

R.adj = [N1] 
N1.adj = [N2, N4, N5, R]
N2.adj = [N3]

N4.adj = [N2, N3, T]

T.adj = [N2]

print(DFS(R,N5))
  

