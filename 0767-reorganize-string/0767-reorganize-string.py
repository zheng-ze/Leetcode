class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if counts.most_common(1)[0][1] >  (len(s) + 1) // 2:
            return ""
        most_common = counts.most_common(1)[0]
        out = [0] * len(s)
        idx = 0
        for i in range(most_common[1]):
            out[idx] = most_common[0]
            idx += 2
        
        for (c, num) in counts.items():
            if (c == most_common[0]):
                continue
            for i in range(num):
                if idx >= len(s):
                    idx = 1
                
                out[idx] = c
                idx += 2
                
            
        return "".join(out)
        