
class Node:
  def __init__(self, data):
    self.data = data
    self.children = []

'''
this function defines what has to be done with the node being visited: it is the one that has to be used to make the desired operation on the visited node
'''
def visit_node(node):
  return node


def DFS(node, visited_nodes = None):
  if visited_nodes is None:
    visited_nodes = {}
  if node is None or node in visited_nodes:
    return []
  dfs = []
  visited_nodes.add(node)
  for n in node.children:    
    dfs += DFS(n, visited_nodes)
  dfs += [visit_node(node)]
  return dfs



R = Node(1)

N1 = Node(2)
N2 = Node(3)
N3 = Node(4)
N4 = Node(5)
N5 = Node(6)

R.children = [N1] 
N1.children = [N2, N4, N5]
N2.children = [N3]
N3.children = [N4]

nodes_order = DFS(R)
for i in nodes_order: 
  print(i.data)
  

