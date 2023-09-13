class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        numChild = len(ratings)
        candies = [1 for i in range(numChild)]
        
        # Do passes. Each in opposite directions. Ensure the neighbour in the direction
        # of travel satisfies condition.
        for i in range(1, numChild):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Since the loop above is from left to right, if right neighbour is lesser than current
        # it does not get updated.
        for i in range(numChild - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
        
        return sum(candies)