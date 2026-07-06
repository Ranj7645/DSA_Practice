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
def left_view_of_binary_tree(root):
    if root is None:
        return
    ans = deque([root])
    while ans:
        size = len(ans)
        for i in range(size):
            curr = ans.popleft()
            if i == 0:



left_view_of_binary_tree(root)