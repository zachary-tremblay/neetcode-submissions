class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = 101
        maxProfit = 0
        for n in prices:
            if n < minValue:
                minValue = n
            if n - minValue > maxProfit:
                maxProfit = n - minValue
        return maxProfit
        
        