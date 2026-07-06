
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
# METHOD -------------------------------- -------------------------  ---------- > 1
def level_order_traversal1(root):
    if root is None:
        return

    q = deque([root])
    q.append(None)

    while len(q)>1:  # important condition , because at end None is left in list
        curr = q.popleft()
        if not curr:
            print(" ")
            q.append(None)
        else:
            print(curr.val, end=" ")

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

level_order_traversal1(root)
print()
print( "method --------- 2")
# Method -------------------------------- --------------- ------------ > 2

def level_order_traversal2(root):
    if root is None:
        return

    q = deque([root])
    while q:
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            print(curr.val, end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        print(" ")
level_order_traversal2(root)