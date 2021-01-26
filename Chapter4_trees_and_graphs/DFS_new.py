
class Node:
  def __init__(self, data):
    self.data = data
    self.adj = []

'''
this function defines what has to be done with the node being visited: it is the one that has to be used to make the desired operation on the visited node
'''
def visit_node(node):
  return node.data


def DFS_visit(n, dfs, visited_nodes):
    
  for v in n.adj:
    if v not in visited_nodes:  
      visited_nodes.add(v)       
      DFS_visit(v, dfs, visited_nodes) 
      dfs += [visit_node(v)]

def DFS(N):
  
  dfs = []
  visited_nodes = set()
  for n in N:
    if n not in visited_nodes:
      visited_nodes.add(n)
      DFS_visit(n, dfs, visited_nodes)
      dfs += [visit_node(n)]
      
  return dfs

R = Node(1)

T = Node(8)

N1 = Node(2)
N2 = Node(3)
N3 = Node(4)
N4 = Node(5)
N5 = Node(6)

R.adj = [N1] 
N1.adj = [N2, N4, N5]
N2.adj = [N3]

N4.adj = [N2, N3, T]

T.adj = [N2]

nodes = [R,T, N1, N2, N3, N4]
nodes_order = DFS(nodes)

print(nodes_order)


