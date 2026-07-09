# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        res = []

        while q:
            last = None
            qLen = len(q)
            for i in range(qLen):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                
                if i == qLen -1:
                     current = q.popleft().val
                else:
                    q.popleft()
            res.append(current)
        return res
