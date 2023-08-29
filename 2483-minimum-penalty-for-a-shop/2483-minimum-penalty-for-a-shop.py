class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Idea to do 2 passes. 1 pass from the left to calculate the penalty incurred from shop being
        open with no customers. Another pass from the right to calculate the penalty incurred from
        shop being closed but customer come.
        """
        hours = len(customers)
        openPenalty = [0 for i in range(hours + 1)]
        closedPenalty = [0 for i in range(hours + 1)]
        
        penalty = 0
        for hour in range(hours):
            openPenalty[hour] = penalty
            penalty += customers[hour] == 'N'
        openPenalty[hours] = penalty
        
        penalty = 0
        for hour in reversed(range(hours)):
            closedPenalty[hour + 1] = penalty
            penalty += customers[hour] == 'Y'
        closedPenalty[0] = penalty
        
        lowest, idx = float('inf'), -1
        for hour in range(len(openPenalty)):
            penalty = openPenalty[hour] + closedPenalty[hour]
            if penalty < lowest:
                lowest = penalty
                idx = hour
        return idx
            