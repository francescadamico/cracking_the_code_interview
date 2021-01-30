'''
You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (travelling only from parent nodes to child nodes).
'''

class Node:

  def __init__(self, data, left = None, right = None):
    self.value = data
    self.left = left
    self.right = right


def paths_with_sum(node, summ, curr_sum = None):

  if curr_sum == None:
    curr_sum = []

  count = 0	
  if node == None:
    
    return count

  curr_sum += [0]
  for i in range(len(curr_sum)):
    curr_sum[i] += node.value
    if curr_sum[i] == summ:
      count += 1
  print(curr_sum)
	
	
  count += paths_with_sum(node.left, summ, curr_sum)
  count += paths_with_sum(node.right, summ, curr_sum) 
  curr_sum.pop()
  for i in range(len(curr_sum)):
    curr_sum[i] -= node.value

  return count



N1 = Node(1)
N2 = Node(2)
N3 = Node(2)
N4 = Node(5)
N5 = Node(-2)
N6 = Node(2)
#N7 = Node(-1)
N8 = Node(3)
N9 = Node(-3)
N10 = Node(5)
N11 = Node(7)

N1.left = N2
N1.right = N9
N2.left = N3
N2.right = N6
N3.left = N4
N3.right = N5
#N6.left = N7
N6.right = N8
N9.left = N10
N9.right = N11

print(paths_with_sum(N1,5))



