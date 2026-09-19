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

# Method -------------------------------------------- 1   (Recurssive)
def inserting_in_binary_tree(Node,val):
    if Node is None:
        return Tree(val)
    
    if val > Node.val:
        Node.right = inserting_in_binary_tree(Node.right,val)
        
    elif val < Node.val:
        Node.left = inserting_in_binary_tree(Node.left,val)
        
    else:
        return Node # Suppose equal value is already present
        
    return Node

ans = inserting_in_binary_tree(root,19)
print(f" Inserting in Binary tree recursivelly", ans.val)
# Method -------------------------------------------- 2   (iterative)
def inserting_in_binary_tree_iterative(Node,val):
    temp = Tree(val)
    parent_node = None
    while Node is not None:
        parent_node = Node
        if val > Node.val:
            Node = Node.right
            
        elif val < Node.val:
            Node = Node.left
        else:
            return Node
                
    if parent_node is None:
        return temp
    
    if parent_node.val > val:
        parent_node.left = temp
        
    else:
        parent_node.right = temp
        
ans = inserting_in_binary_tree_iterative(root,10)

# i was just checking is it inserted perfectly or not
def dfs(root):
    if root is None:
        return
    print(root.val,end=" ")
    dfs(root.left)
    dfs(root.right)
    
dfs(root)
    
    