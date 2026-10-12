class Node:
    def __init__(self,v):
        self.right = None
        self.left = None
        self.data = v

root = Node(100)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(70)
root.right.left = Node(90)
root.right.right = Node(400)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

#inorder - 40 20 70 90 30 400
#preorder - 100 20 40 70 30 90 400
#postorder - 40 70 20 90 400 30 100

print("Inorder travelsal: ")
inorder(root)

print("Preorder traversal: ")
preorder(root)

print("Postorderr traversal:")
postorder(root)