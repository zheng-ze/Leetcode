class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        out = 0

        if rungs[0] > dist: 
            out += math.floor((rungs[0] - 1) / dist)
        
        for i in range(1, len(rungs)):
            if rungs[i] - rungs[i - 1] > dist:
                out += math.floor((rungs[i] - rungs[i - 1] - 1) / dist)
        return out