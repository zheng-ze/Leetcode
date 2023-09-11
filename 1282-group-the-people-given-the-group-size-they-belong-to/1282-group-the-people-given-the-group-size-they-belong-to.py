class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        out = []
        d = {}
        
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            
            if size in d:
                d[size].append(i)
            else:
                d[size] = [i]
                
            if len(d[size]) == size:
                out.append(d.pop(size))
            
        
        return out