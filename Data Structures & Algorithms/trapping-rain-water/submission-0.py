class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        lMax = 0
        rMax = 0
        prefix = []
        suffix = []
        for i in range(len(height)):
            lMax = max(lMax, height[i])
            prefix.append(lMax)
            rMax = max(rMax, height[len(height)-1-i])
            suffix.append(rMax)
        suffix.reverse()

        for i, n in enumerate(height):
            res += min(prefix[i], suffix[i]) - n
        return res
