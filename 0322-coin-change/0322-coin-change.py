class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] < float('inf') else -1