class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        curr = []

        def dfs(i):
            currSum = sum(curr)
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i+1)
            curr.pop()

            while i < len(candidates)-1 and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res
        