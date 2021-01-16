'''
Write an algorithm to find the 'next' node (i.e. in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.parent = None
  

def bottom_left(n):
  if n.left == None:
    return n    
  return bottom_left(n.left)
  
  
def next(n):
  if n.right == None:
    if n.parent.right == n:
      return n.parent.parent 
    else: # n.parent.left == n
      return n.parent
  else:
    return bottom_left(n.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(4)
n4 = Node(7)
n5 = Node(12)
n6 = Node(10)
n7 = Node(15)
n8 = Node(20)
n9 = Node(14)


n1.parent = n2
n3.parent = n2

n2.left = n1
n2.right = n3
n2.parent = n4


n4.left = n2
n4.right = n5

n5.left = n6
n5.right = n7
n5.parent = n4

n6.parent = n5

n7.right = n8
n7.left = n9
n7.parent = n5

n8.parent = n7

n9.parent = n7


print(next(n5).data)



