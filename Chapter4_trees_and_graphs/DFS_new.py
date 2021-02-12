def visit_node(n):
	return n*2

def DFS_visit(N, n, visited_nodes, DFS):
  for v in N[n]:
    if v not in visited_nodes:
      visited_nodes.add(v)
      DFS += [visit_node(v)]
      DFS_visit(N, v, visited_nodes, DFS)
			


def DFS(N):
  visited_nodes = set()
  DFS = []
  for n in N.keys():
    if n not in visited_nodes:
      visited_nodes.add(n)
      DFS += [visit_node(n)]
      DFS_visit(N, n, visited_nodes, DFS)
      
  
  return DFS



N = {
'a':['b', 'e'],
'b':['c', 'd'],
'c':[],
'd':['e'],
'e':[],
'f':[]
}

print(DFS(N))


