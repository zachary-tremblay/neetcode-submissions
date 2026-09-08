class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for n in coins:
            for i in range(amount+1):
                if i-n >= 0 and dp[i-n] >= 1:
                    dp[i] += dp[i-n]
        return dp[-1]