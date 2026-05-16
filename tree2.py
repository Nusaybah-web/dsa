class tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def inorder(root):
    if root is not None:
        if root.left is not None:
            inorder(root.left)
        print(root.data)
        if root.right is not None:
            inorder(root.right)
        print(root.data)

def insert(root,value):
    if root==None:
        return tree(value)
    if root.data>value:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root

def search(root,find):
    if root.data==find:
        return root
    elif root.data>find and root.left is not None:
        return search(root.left,find)
    elif root.data<find and root.right is not None:
        return search(root.left,find)
    else:
        return -1

num=int(input("how many elements do you want: "))
root=None

for i in range(num):
    data=int(input("enter the node value: "))
    root=insert(root,data)

inorder(root)

find=int(input("enter the value you want to find: "))

findnode=search(root,find)

if findnode==-1:
    print("key dose not exist in the tree")
else:
    print("key exists",findnode.data)