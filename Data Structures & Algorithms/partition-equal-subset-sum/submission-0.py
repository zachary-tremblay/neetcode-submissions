class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total %2 != 0:
            return False

        target = total / 2
        sums = set()
        sums.add(0)

        for n in nums:
            newSums = set()
            for t in sums:
                if t + n == target:
                    return True
                newSums.add(t+n)
                newSums.add(t)
            sums = newSums
        return False
        

        

