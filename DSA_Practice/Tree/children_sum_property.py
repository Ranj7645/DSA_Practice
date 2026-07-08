class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(20)
root.left.right =Node(12)
root.right = Node(30)
root.right.right = Node(50)
root.right.left = Node(40)
root.right.left.right = Node(90)
root.right.right.right = Node(60)
'''
     10
    /  \
  20     30
   \      / \
    12  40    50
          \       \
           90      60
'''
from collections import deque
def child_sum(root):
    if root is None:
        return
    q = deque([root])

    while len(q) > 0:
        size = len(q)
        for i in range(size):
