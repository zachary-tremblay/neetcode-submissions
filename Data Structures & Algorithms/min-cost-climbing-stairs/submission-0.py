class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sumCost = [0] * (len(cost))
        sumCost[0], sumCost[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            sumCost[i] = min(sumCost[i-1], sumCost[i-2]) + cost[i]
        
        return min(sumCost[-1], sumCost[-2])

        
        
        