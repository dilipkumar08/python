#Binary tree

class node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(4)
    root.left.left=node(4)
    root.left.right=node(8)
    root.right.left=node(8)
    root.right.right=node(16)
    print("pre-order:")
    root.preorder()
    print("post-order:")
    root.postorder()
    print("in-order:")
    root.inorder()
