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
        
        
        # fill will always point to outermost node that is smaller than x
        # i.e the area that is "solved"
        # Nodes between fill and head will be those that don't meet the criteria
        while head.next:
            # current node is less than x -> new fill position
            if head.val < x:
                fill = head
                head = head.next
                continue
            # current node does not meet criteria but next node does -> swap
            if head.val >= x and head.next.val < x:
                temp = head.next
                head.next = head.next.next
                temp.next = fill.next
                fill.next = temp
                fill = fill.next
            # current node does not meet criteria but next node also doesn't -> move on to find one that does    
            else:
                head = head.next
            
        
        return out.next