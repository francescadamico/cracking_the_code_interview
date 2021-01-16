

class Node:
  def __init__(self, data):
    self.data = data
    self.adj = []

def visit(n):
  return n.data

def BFS(n):
  level = {n: 0}
  i = 1
  frontier = [n]
  visited_nodes = []
  while frontier:
    next = []
    for u in frontier:
      for v in u.adj:
        if v not in level:
          level[v] = i
          next.append(v)
          visited_nodes.append(visit(v))
    frontier = next
    i += 1
  return visited_nodes


R = Node(1)

N1 = Node(2)
N2 = Node(3)
N3 = Node(4)
N4 = Node(5)
N5 = Node(6)

R.adj = [N1] 
N1.adj = [N2, N4, N5]
N2.adj = [N3]
N3.adj = [N4]

nodes_order = BFS(R)
print(nodes_order)

  


