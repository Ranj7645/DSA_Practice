class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.right = Node(50)
root.right.left = Node(40)
'''
     10
    /  \
  20     30
         /  \
      40      50
'''

def preorder_traversel(root):
    if root is None:
        return
    print(root.val,end=" ")
    preorder_traversel(root.left)
    preorder_traversel(root.right)


def inorder_traversel(root):
    if root is None:
        return
    inorder_traversel(root.left)
    print(root.val,end=" ")
    inorder_traversel(root.right)

print ("postorder traversel \n")

def postorder_traversel(root):
    if root is None:
        return
    postorder_traversel(root.left)
    postorder_traversel(root.right)
    print(root.val,end=" ")

preorder_traversel(root)
print("preorder \n")
inorder_traversel(root)
print ("inorder traversel \n")
postorder_traversel(root)
print("post_order\n")


