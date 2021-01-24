'''
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None
    self.parent = None
    
  def anchestors(self):
    anchestors = []
    node = self
    while node:
      anchestors.append(node)
      node = node.parent
    return anchestors
  
  def first_common(self, other):
    other_anchestors = set(other.anchestors())
    node = self
    while node:
      if node in other_anchestors:
        return node
      node = node.parent
    return None

def find_level(a, level = 1):

  if a.parent == None:
    return level
  level += 1
  a = a.parent
  return find_level(a, level)
  

def swap(a, b):

  a.data, b.data = b.data, a.data

  return a, b
  

def bring_same_level(a, b):
  
  la = find_level(a)
  lb = find_level(b)  

  x, y = a, b

  while la != lb:
    if la < lb:
      b, b.parent = swap(b, b.parent)
      lb -= 1
      y = b.parent
    else:
      a, a.parent = swap(a, a.parent)
      la -= 1
      x = a.parent

  return x, y

def find_ancestor(a, b):

  if a.parent.data == b.parent.data:
    return a.parent

  a, a.parent = swap(a, a.parent)
  b, b.parent = swap(b, b.parent)
  
  return find_ancestor(a.parent, b.parent)


def common_ancestor(a, b):

  new_a, new_b = bring_same_level(a, b)

  return find_ancestor(new_a, new_b)



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3

n2.left = n4
n2.parent = n1
n6.parent = n3

n3.left = n7
n3.right = n6

n4.parent = n2

n3.parent = n1
n7.parent = n3


print(common_ancestor(n4, n7).data)
