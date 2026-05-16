class tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

root=tree(3)
def findmax(root):
    if root is None:
        return -1000
    leftmax=findmax(root.left)
    rightmax=findmax(root.right)
    return max(root.data,leftmax,rightmax)

root.left=tree(4)
root.right=tree(5)

root.left.left=tree(6)
root.left.right=tree(7)

root.right.left=tree(8)
root.right.right=tree(9)

print("maximum value is: ",findmax(root))