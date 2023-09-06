# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Get length of linked list
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        # Get number of nodes in each part
        numEachPart = l // k
        remainder = l % k
        
        out = []
        curr = head
        
        for i in range(k):
            out.append(curr)
            last = None
            for j in range(numEachPart + (1 if remainder > 0 else 0)):
                last = curr
                curr = curr.next
            
            if last != None:
                last.next = None
        
            remainder -= 1
        
        return out
        