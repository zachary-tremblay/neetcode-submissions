class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0:0, 1:0, 2:0}
        for n in nums:
            freq[n] += 1

        nums[:] = [0] * freq[0] + [1] *freq[1] + [2] * freq[2]
        