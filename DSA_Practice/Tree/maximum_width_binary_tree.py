class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

root = Node(10)
root.left = Node(20)
root.left.right =Node(12)
root.left.left =Node(121)
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
from collections import deque

class FindiningMaxWidth():

    def maximum_width_binary_tree(self,root_node):
        result = 0
        if root_node is None:
            return
        q = deque([root_node])
        while q:
            temp_len = len(q)
            counter = 0
            for i in range(temp_len):
                temp_node = q.popleft()
                if temp_node.left is not None:
                    q.append(temp_node.left)

                if temp_node.right is not None:
                    q.append(temp_node.right)

                counter+=1
            result = max(result,counter)
        return result
finding_max_width = FindiningMaxWidth()
result = finding_max_width.maximum_width_binary_tree(root)
print(result)