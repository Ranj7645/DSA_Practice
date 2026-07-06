
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
root.right.right.right = Node(60)
'''
     10
    /  \
  20     30
   \      / \
    12  40    50
                 \
                  60
'''
from collections import deque

def level_order_traversal(root):
    if root is None:
        return

    q = deque([root])

    while q:
        node = q.popleft()

        print(node.val, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

level_order_traversal(root)

