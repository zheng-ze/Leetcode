from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:        
        @lru_cache(None)
        def dp(currPos, M):
            if currPos + 2 * M >= N: # Legal to collect all remaining piles so collect all
                return piles[currPos] 
            
            # Make the decision that will result in lowest wins for opponent as both players are rational
            return piles[currPos] - min(dp(currPos + numPilesToTake, max(M, numPilesToTake)) for numPilesToTake in range(1, 2 * M + 1))
        
        N = len(piles)
        
        # Computes the maximum stones obtainable if all stones from current pile is collected.
        # Allows for easy computation later on when determining optimal decision
        for i in range(N - 2, -1, -1): 
            piles[i] += piles[i + 1]
        
        return dp(0, 1)