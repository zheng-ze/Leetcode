class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if detail[11:13] <= "60":
                continue
            
            count += 1
        
        return count