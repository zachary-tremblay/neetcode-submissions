# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, previousMax):
            nonlocal res
            if root.val >= previousMax:
                res += 1
            if root.left:
                dfs(root.left, max(previousMax, root.val))
            if root.right:
                dfs(root.right, max(previousMax, root.val))
        dfs(root, float("-infinity"))
        return res