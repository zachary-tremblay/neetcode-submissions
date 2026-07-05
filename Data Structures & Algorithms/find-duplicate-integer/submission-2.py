class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i]) -1
            print(idx)
            if nums[idx] < 0:
                return abs(nums[i])
            else:
                nums[idx] = -nums[idx]
        return -1
