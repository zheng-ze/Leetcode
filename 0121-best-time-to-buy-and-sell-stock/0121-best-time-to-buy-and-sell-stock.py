class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minBuy, maxProfit = float('inf'), 0
        
        for price in prices:
            minBuy = min(minBuy, price)
            # Profit calculated if sold at current price when bought at the seen min price
            maxProfit = max(maxProfit, price - minBuy)
            
        return maxProfit