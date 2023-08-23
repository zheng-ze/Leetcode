import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if counts.most_common(1)[0][1] >  (len(s) + 1) // 2:
            return ""
        pq = [(-val, c) for (c, val) in counts.items()]
        heapq.heapify(pq)
        
        prev_val, prev_c = 0, ""
        out = []
        
        while pq:
            if (prev_val < 0):
                val, c = heapq.heapreplace(pq, (prev_val, prev_c))
            else:
                val, c = heapq.heappop(pq)
            
            out.append(c)
            prev_val = val + 1
            prev_c = c
                
        return "".join(out)
        