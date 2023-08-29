class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Calculate the maximal profit for opening until that hour
        """
        maxProfit = 0
        profitHour = 0
        currProfit = 0
        for hour, customer in enumerate(customers):
            currProfit += (1 if customer == 'Y' else -1)
            
            if currProfit > maxProfit:
                profitHour = hour + 1
                maxProfit = currProfit
        
        return profitHour