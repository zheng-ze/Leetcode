# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list nothing to swap
        if head == None:
            return head
        
        # Pointer to start
        startPointer = ListNode(None, head)
        
        # Pointer to the start of initial pair
        currPointer = head
        
        # Pointer to end of the dummy previous pair
        prevPointer = startPointer
        
        # while pairs are valid
        while currPointer and currPointer.next:
            # Get node next to current node
            adjPointer = currPointer.next
            
            # Remember the node for next iteration
            nextPointer = adjPointer.next
            
            # Swap order of the pairs
            adjPointer.next = currPointer
            currPointer.next = nextPointer
            
            # Set the next of previous pair to start of interverted current pair
            prevPointer.next = adjPointer
            
            # Remember the end of the current pair
            prevPointer = currPointer
            
            # Shift to next pair
            currPointer = nextPointer
            
            
            
        return startPointer.next