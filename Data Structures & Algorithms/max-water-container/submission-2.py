class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
    
        while (l < r):
            curr = min(heights[l], heights[r]) * (r - l) 
            if curr > res:
                res = curr
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return res
            
        