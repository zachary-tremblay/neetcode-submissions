class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        hm = {}
        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        
        hm2 = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))
        return list(hm2.keys())[:k]
        

        
        


        