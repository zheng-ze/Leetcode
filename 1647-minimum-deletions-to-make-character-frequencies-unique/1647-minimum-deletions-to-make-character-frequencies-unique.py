class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
                
        d = {}
        same = []
        for elem in counts.keys():
            if counts[elem] in d:
                same.append((elem, counts[elem]))
            else:
                d[counts[elem]] = elem
        
        if len(same) == 0:
            return 0
        out = 0
        for (elem, freq) in same:
            while freq > 0:
                if freq not in d:
                    d[freq] = elem
                    break
                out += 1
                freq -= 1
        
        return out
                    