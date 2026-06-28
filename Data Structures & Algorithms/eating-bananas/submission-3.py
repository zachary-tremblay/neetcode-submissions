class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        if h == len(piles):
            return piles[-1]

        total = 0

        left = 1
        right = piles[-1]
        valid = 0
        while left <= right:

            mid = (left + right) // 2
            time = 0
            for b in piles:
                time = 0
                for b in piles:
                    time += math.ceil(b / mid)
            if time <= h:
                valid = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return valid
            

        


