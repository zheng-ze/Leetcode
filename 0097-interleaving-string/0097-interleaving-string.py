class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If length does not match, impossible for it to be an interleaving.
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        if l1 + l2 != l3:
            return False
        
        # Idea to do BFS, find all possible combis until one of them reaches the end.
        q = deque([(0, 0)])
        visited = set()
        
        while q:
            idx1, idx2 = q.popleft()
            
            if (idx1, idx2) in visited:
                continue
            
            visited.add((idx1, idx2))
            
            if idx1 + idx2 == l3:
                return True
            
            if idx1 + 1 <= l1 and s1[idx1] == s3[idx1 + idx2]:
                q.append((idx1 + 1, idx2))
            
            if idx2 + 1 <= l2 and s2[idx2] == s3[idx1 + idx2]:
                q.append((idx1, idx2 + 1))

        return False
                