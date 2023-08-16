class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        
        if k == length:
            return [max(nums)]
        
        out = [0] * (length - k + 1)
        window = deque([])
        
        for i in range(length):
            # Remove indexes that are no longer part of the window
            while window and i - window[0] >= k:
                window.popleft()
                
            # Remove indexes with num < curr num. They will never be the max of any sliding window
            # since curr num is larger and will exist longer than them.
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            
            window.append(i)
            
            if (i >= k - 1):
                out[i - k + 1] = nums[window[0]]
                
        return out