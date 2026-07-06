class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

root = Node(10)
root.left = Node(5)
root.right = Node(15)
print(root.val,"ddf", root.left.val,"fewffe",root.right.val)