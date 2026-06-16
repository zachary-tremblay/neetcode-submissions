class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        runningPrefix = 1
        for i in range(len(nums)):
            output[i] = runningPrefix
            runningPrefix *= nums[i]
        runningSuffix = 1 
        for i in range(len(nums)-1, -1, -1):
            output[i] *= runningSuffix 
            runningSuffix *= nums[i]
        return output
        