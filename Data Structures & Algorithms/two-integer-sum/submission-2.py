class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hs:
                return [hs[diff], i]
            else:
                hs[n] = i