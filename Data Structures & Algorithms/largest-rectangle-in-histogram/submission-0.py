class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, n in enumerate(heights):
            start = i
            while stack and stack[-1][0] > n:
                height, index  = stack.pop()
                res = max(res, (i - index) * height)
                start = index
                
            stack.append((n, start))

        for n, i in stack:
            res = max(res, n * (len(heights) - i))

        return res