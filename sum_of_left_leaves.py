# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def node_sum(node,left):
            if not node:
                return
            node_sum(node.right,False)
            node_sum(node.left,True)
            
            if not node.right and not node.left and left:
                self.total+=node.val
        node_sum(root,False)
        return self.total
