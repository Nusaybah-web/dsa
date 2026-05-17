class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,key):
    if root is None:
        return tree(key)
    elif key<root.data:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def findmin(root):
    current=root
    while current.left:
        current=current.left
    return current

def delete(root,key):
    if root is None:#tree is empty
        return root
    elif key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp=findmin(root.right)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root

root=None

num=int(input("enter the number of nodes that you want: "))

for i in range(num):
    value=int(input("please insert a value: "))
    root=insert(root,value)

print("inorder triversal", inorder(root))

dele=int(input("what value do you want to delete: "))

root=delete(root,dele)

print("tree after deletion ", inorder(root))