class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mySet = set()
        rangeMax = float("-inf")
        rangeMin = float("inf")
        for n in nums:
            if n > rangeMax:
                rangeMax = n
            if n < rangeMin:
                rangeMin = n
            mySet.add(n)
        counter = 0
        maxSequence = 0
        for i in range(rangeMin-1, rangeMax+1):
            if i+1 in mySet:
                counter +=1
            else:
                if counter > maxSequence:
                    maxSequence = counter
                counter = 0
            
        return maxSequence