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
# method - 1 is using time complexity of O(N)**2
def is_balanced_tree(node):
    if node is None:
        return True
    lh = height_of_tree(node.left)
    rh = height_of_tree(node.right)
    return abs(rh-lh) <=1 and is_balanced_tree(node.left) and is_balanced_tree(node.right)

result = is_balanced_tree(root)
print(result)

# Method ---- 2 Is using time complexity of O(N)

def is_balanced_2(node):
    if node is None:
        return 0

    lh = is_balanced_2(node.left)
    if lh == -1:
        return -1

    rh = is_balanced_2(node.right)
    if rh == -1:
        return -1

    if abs( rh - lh ) > 1:
        return -1
    else:
        return max(lh,rh)+1

result_1 = is_balanced_2(root)
if result_1 == -1:
    result_1 = False
else:
    result_1 = True
print(result_1)