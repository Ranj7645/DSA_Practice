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

#  Find the node value at k distance  method -- 1
k = 2
def printing_node_at_k_distance(root,k):
    if root is None:
        return
    if k == 0:
        print(root.val)
        return

    printing_node_at_k_distance(root.left,k-1)
    printing_node_at_k_distance(root.right, k - 1)

printing_node_at_k_distance(root,k)
print ("Method ---- ------------- ------- 2")
#  Find the node value at k distance  method -- 2
def printing_node_at_k_distance2(root,k):
    if root is None:
        return []
    if k == 0:
        return [root.val]

    left = printing_node_at_k_distance2(root.left,k-1)
    right = printing_node_at_k_distance2(root.right, k - 1)
    left.extend(right)
    return left

result = printing_node_at_k_distance2(root,k)
print(f"result of method 2 is : {result}")