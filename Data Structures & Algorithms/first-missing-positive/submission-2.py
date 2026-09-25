class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0
        
        for n in nums:
            if abs(n)-1 < len(nums) and abs(n)-1 >= 0:
                if nums[abs(n)-1] == 0:
                    nums[abs(n)-1] = -1*(len(nums)+1)
                elif nums[abs(n)-1] > 0:
                    nums[abs(n)-1] *= -1
        
        for i, n in enumerate(nums):
            if n >= 0:
                return i+1

        return len(nums)+1
        