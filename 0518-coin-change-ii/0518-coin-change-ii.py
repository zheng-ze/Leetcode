class Solution:        
    def change(self, amount: int, coins: List[int]) -> int:
        self.dp = [0] * (amount + 1)
        self.dp[0] = 1
        for coin in coins:
            for val in range(coin, amount + 1):
                self.dp[val] += self.dp[val - coin]
        
        return self.dp[amount]
            
        