class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        amounts = [float("inf")]*(amount+1)

        for value in coins:
            if len(amounts) > value:
                amounts[value] = 1
        
        for i in range(len(amounts)):
            for value in coins:
                if i-value > 0:
                    amounts[i] = min(amounts[i-value]+1, amounts[i])
        
        return amounts[-1] if amounts[-1] < float("inf") else -1


