class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        space = [0 for i in range(len(capacity))]
        for i in range(len(capacity)):
            space[i] = capacity[i] - rocks[i]
        space.sort()
        num = 0
        for s in space:
            if not s:
                num += 1
            if s:
                if additionalRocks >= s:
                    additionalRocks -= s
                    num += 1
        return num