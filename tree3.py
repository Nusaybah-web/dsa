class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def find(root):
    while root.left is not None:
        root=root.left
    return root.data

root=tree(3)

root.left_child=tree(4)
root.right_child=tree(5)

root.left_child.left_child=tree(6)
root.left_child.right_child=tree(7)

root.right_child.left_child=tree(8)
root.right_child.right_child=tree(9)

print(find(root))