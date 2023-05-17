# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Reverse 1st half of the linked list so that we can iterate through
        # both linked list at the same time for pair
        slowPointer = head
        fastPointer = slowPointer

        # slowPointer reaches midpoint and fastPointer reaches end
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        prev = None

        # Reverse first half. slowPointer is start of 2nd half
        while head != slowPointer:
            nextNode = head.next
            head.next = prev

            prev = head
            head = nextNode
                
        # head points to start of newly reversed list
        head = prev
        
        maxSum = 0

        # Iterate both halves and find maximum sum of pair so far
        while head and slowPointer:
            maxSum = max(head.val + slowPointer.val, maxSum)

            head = head.next
            slowPointer = slowPointer.next
        
        return maxSum