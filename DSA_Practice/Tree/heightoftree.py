class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

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

def height_of_tree(root):
    if root is None:
        return 0
    left = height_of_tree(root.left)
    right = height_of_tree(root.right)
    return max(left,right)+1

height = height_of_tree(root)
print("height : ", height)


