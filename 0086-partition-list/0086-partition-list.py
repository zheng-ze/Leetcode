# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        fill = ListNode(None, head)
        out = fill
        
        while head.next:
            if head.val < x:
                fill = fill.next
                head = head.next
                continue
            if head.val >= x and head.next.val < x:
                temp = head.next
                head.next = head.next.next
                temp.next = fill.next
                fill.next = temp
                fill = fill.next
            else:
                head = head.next
            
        
        return out.next