class Tree:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        
# inserting the value in BST
root = Tree(15)
root.left = Tree(5)
root.left.left = Tree(3)

root.right = Tree(20)
root.right.left = Tree(18)
root.right.left.left = Tree(16)
root.right.right = Tree(80)
'''
        15
      /   \
     5     20
    /      / \
   3      18  80
          /
        16
'''
# Recurssive method
def search(Node,val):
    if Node is None:
        return False
    
    if Node.val == val:
        return True
    
    if Node.val < val:
        return search(Node.right,val)
        
    elif Node.val > val:
        return search(Node.left,val)
        
ans = search(root,18)
print(f"did we find the number ? {ans}")

# Iterative method

def search(Node,val):
    while Node is not None:
        if Node.val == val:
            return True
        
        if Node.val < val:
            Node = Node.right
            
        elif Node.val > val:
            Node = Node.left

    return False
ans = search(root,18)
print(f"did we find the number ? {ans}")