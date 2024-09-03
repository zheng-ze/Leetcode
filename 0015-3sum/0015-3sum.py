from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        out = []
        positives, negatives, zeros = defaultdict(int), defaultdict(int), 0
        
        for num in nums:
            if num > 0:
                positives[num] += 1
            elif num < 0:
                negatives[num] += 1
            elif zeros < 3:
                zeros += 1
        
        if zeros >= 3:
            out.append([0, 0, 0])
            
        posNums = list(positives.keys())
        negNums = list(negatives.keys())
        
        for i in range(len(posNums)):
            num = posNums[i]
            if -num in negatives and zeros > 0:
                out.append([num, 0, -num])
            
            if positives[num] > 1 and num * -2 in negatives:
                out.append([num, num, num * -2])
            
            for j in range(i + 1, len(posNums)):
                num2 = posNums[j]
                negNum = -(num + num2)
                if negNum in negatives:
                    out.append([num, num2, negNum])
                
        for i in range(len(negNums)):
            num = negNums[i]
            
            if negatives[num] > 1 and num * -2 in positives:
                out.append([num, num, num * -2])
            
            for j in range(i + 1, len(negNums)):
                num2 = negNums[j]
                posNum = -(num + num2)
                if posNum in positives:
                    out.append([num, num2, posNum])
        
        return out
            
            