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
max_height = 0
def left_view_of_binary_tree_recurssive(root,height):

    global max_height
    if root is None:
        return
    if max_height < height:
        print(root.val)
        max_height = height
    left_view_of_binary_tree_recurssive(root.left, height+1)
    left_view_of_binary_tree_recurssive(root.right, height + 1)

from collections import deque
def left_view_of_binary_tree_iterative(node):
    if node is None:
        return

    q = deque([node])
    while len(q)>0:
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            if i==0:
                print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

left_view_of_binary_tree_recurssive(root,1)
print("method ------------------------ --------------------  -------------------- 2")
left_view_of_binary_tree_iterative(root)