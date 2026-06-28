class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("infinity")

        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            res = min(res, nums[mid])
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        return res