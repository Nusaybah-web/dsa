class tree:
    def __init__(self,data):
        self.data=data
        self.left_child=None
        self.right_child=None

root=tree(3)

root.left_child=tree(4)
root.right_child=tree(5)

root.left_child.left_child=tree(6)
root.left_child.right_child=tree(7)

root.right_child.left_child=tree(8)
root.right_child.right_child=tree(9)

def preordertriversal(node):
    if node is not None:
        print(node.data)
        preordertriversal(node.left_child)
        preordertriversal(node.right_child)

print("preordertriversal ")
preordertriversal(root)

def inorder(node):
    if node is not None:
        inorder(node.left_child)
        print(node.data)
        inorder(node.right_child)
    
print("inorder ")
inorder(root)

def postorder(node):
    if node is not None:
        postorder(node.left_child)
        postorder(node.right_child)
        print(node.data)


print("postorder ")
postorder(root)