class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        rob1, rob2, rob3, rob4 = 0, 0, 0, 0

        for i in range(len(nums)-1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp

            temp2 = max(rob3 + nums[i+1], rob4)
            rob3 = rob4
            rob4 = temp2
        
        return max(rob2, rob4)