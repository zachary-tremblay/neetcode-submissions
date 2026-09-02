class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        one, two = 0, 0
        for n in nums:
            temp = max(one + n, two)
            one = two
            two = temp
        return two
            


