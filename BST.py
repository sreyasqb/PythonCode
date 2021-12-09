class BST:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def insert(self,root,data):
        if root is None:
            return BST(data)
        else:
            if root.val>data:
                root.left=self.insert(root.left,data)
            else:
                root.right=self.insert(root.right,data)
            return root


root=BST(5)
root.insert(root,6)
root.insert(root,4)
root.insert(root,3)
print(root.left.left.val)

