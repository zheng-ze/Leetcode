class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 1:
            return []
        d = set()
        
        for candidate in candidates:
            if candidate > target:
                continue
            d.add(candidate)
        
        out = []
        def dfs(target, path, paths, floor):
            if target < 0:
                return
            if target == 0:
                paths.append(path)
                return
            for candidate in d:
                if candidate < floor:
                    continue
                dfs(target - candidate, path + [candidate], paths, candidate)
        
        dfs(target, [], out, 2)
        return out
                
                