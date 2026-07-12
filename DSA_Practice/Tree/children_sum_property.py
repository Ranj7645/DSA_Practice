class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(8)
root.left.left =Node(3)
root.right = Node(12)
root.left.right =Node(5)
'''
     20
    /  \
  8     12
 / \     
3   5  
'''

def child_sum_property(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    sum = 0
    if root.left is not None:
        sum += root.left.val
    if root.right is not None:
        sum += root.right.val

    return sum == root.val and child_sum_property(root.left) and child_sum_property(root.right)

print(child_sum_property(root))