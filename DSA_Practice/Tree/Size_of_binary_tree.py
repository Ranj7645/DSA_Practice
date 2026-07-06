from itertools import count


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

def size_of_binary_tree_using_DFS(root):

    if root is None:
        return 0

    left = size_of_binary_tree_using_DFS(root.left)
    right = size_of_binary_tree_using_DFS(root.right)
    return 1+left+right

size = size_of_binary_tree_using_DFS(root)
print(f"Size of tree using DFS {size}")

from collections import deque
def size_of_binary_tree_using_BFS(root):

    if root is None:
        return 0
    q = deque([root])
    size = 0

    while q:
        node = q.popleft()
        print(node.val, end=" ")

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
        size += 1
    return size
size = size_of_binary_tree_using_BFS(root)
print(f"Size of tree using BFS {size}")
