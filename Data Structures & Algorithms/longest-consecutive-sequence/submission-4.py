class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mySet = set()
        for n in nums:
            mySet.add(n)
        counter = 0
        maxSequence = 1
        for n in mySet:
            if (n-1) not in mySet:
                counter =1
                while (n+counter) in mySet:
                    counter +=1
                    if counter > maxSequence:
                        maxSequence = counter
                counter = 0
        return maxSequence