import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        
        # If the most common character is has count > half rounded up, it is impossible 
        # to not have at least 1 instance where the most common character is next to each other
        # Consider the string 'aaaabb', in order to separate the most common character,
        # we need to have another character in between each instance of that character hence
        # we need at least 3 of any other character shown here: a,_,a,_,a,_,a
        if counts.most_common(1)[0][1] >  (len(s) + 1) // 2:
            return ""
        
        # Using a priority queue so that we can resolve for the most frequent chars first
        # Since they require the most number of other characters to separate them.
        pq = [(-val, c) for (c, val) in counts.items()]
        heapq.heapify(pq)
        
        # To prevent repeated use of most frequent, we store the previous and only add them after
        # each iteration
        prev_val, prev_c = 0, ""
        out = [0 for i in range(len(s))]
        idx = 0
        
        while pq:
            if (prev_val < 0):
                # heap replace because it is more efficient
                val, c = heapq.heapreplace(pq, (prev_val, prev_c))
            else:
                val, c = heapq.heappop(pq)
            
            out[idx] = c
            idx += 1
            prev_val = val + 1
            prev_c = c
                
        return "".join(out)
        