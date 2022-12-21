# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slower = head
        faster = head
        
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
        
        return slower