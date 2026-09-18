class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, currSet):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in currSet:
                    curr.append(nums[i])
                    currSet.add(nums[i])
                    dfs(curr, currSet)
                    curr.pop()
                    currSet.remove(nums[i])
        dfs([], set())
        return res
            


