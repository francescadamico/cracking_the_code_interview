

class Node:
  def __init__(self, data):
    self.data = data
    self.adj = []

def visit(n):
  return n.data

def BFS2(root):
  from collections import dequeue
  bfs = []
  stack = dequeue([root])
  visited = {}
  while stack:
    node = stack.popleft()
    visited.add(node)
    bfs.append(node)
    stack.extend([n for n in node.adj if n not in visited])
  return bfs

def recursive_BFS(root, visited = None):
  if visited is None:
    visited = {}
  visited.add(root)
  bfs = [root]
  for node in root.adj:
    if node not in visited:
      bfs.etend(recursive_BFS(node, visited)
  return bfs

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

  


