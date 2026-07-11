# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                if q[0].right:
                    q.append(q[0].right)
                if q[0].left:
                    q.append(q[0].left)

                heapq.heappush(heap, q.popleft().val)
        
        res = None
        for i in range(k):
            res = heapq.heappop(heap)
        return res

        