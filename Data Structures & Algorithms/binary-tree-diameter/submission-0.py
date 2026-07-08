# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.maxDiameter(root)
        return self.res
        
    def maxDiameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = (self.maxDiameter(root.left))
        right = (self.maxDiameter(root.right))
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
        