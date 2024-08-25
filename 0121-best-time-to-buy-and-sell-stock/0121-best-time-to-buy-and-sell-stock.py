class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxProfit = float('inf'), float('-inf')
        
        for price in prices:
            minBuy = min(minBuy, price)
            # Profit calculated if sold at current price when bought at the seen min price
            maxProfit = max(maxProfit, price - minBuy)
            
        return maxProfit