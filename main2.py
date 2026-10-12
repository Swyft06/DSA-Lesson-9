class Node:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v

root = Node(300)
root.left = Node(100)
root.right = Node(200)
root.left.left = Node(30)
root.left.right = Node(50)
root.right.left = Node(20)
root.right.right = Node(60)

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

#inorder - 30 100 50 300 20 200 60
#preorder - 300 100 30 50 200 20 60
#postorder - 30 50 100 20 60 200 300
while True:
    i = input("What traversal would you like to do or type exit to quit ")
    if i == "inorder":
        print("Inorder traversal: ")
        inorder(root)

    elif i == "preorder":
        print("preorder traversal: ")
        preorder(root)

    elif i == "postorder":
        print("postorder traversal: ")
        postorder(root)

    elif i == "exit":
        print("Thank you")
        break

    else:
        print("Invalid input")