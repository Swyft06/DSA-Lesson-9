class Node:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(100)
root.left = Node(50)
root.right = Node(150)
root.left.left = Node(30)
root.left.right = Node(60)
root.right.left = Node(40)
root.right.right = Node(80)

print(count_nodes(root))
