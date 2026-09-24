class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        thresh = len(nums)/3
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, value in freq.items():
            if value > thresh:
                res.append(key)
        return res