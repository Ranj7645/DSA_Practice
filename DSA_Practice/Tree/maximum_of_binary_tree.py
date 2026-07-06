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

def maximum_of_binary_tree(root):
    if root is None:
        return float('-inf')
    left = maximum_of_binary_tree(root.left)
    right = maximum_of_binary_tree(root.right)

    return max(left,right,root.val)

value = maximum_of_binary_tree(root)
print(f"Maximum value of tree is {value}")
