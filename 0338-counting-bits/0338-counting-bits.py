class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0] * (n + 1)
        
        for i in range(1, n + 1):
            num = i
            while num != 0:
                out[i] += num & 1
                num = num >> 1
        
        return out