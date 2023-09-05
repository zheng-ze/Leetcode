from copy import deepcopy

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head or head.next:
            return deepcopy(head)
        
        current = head
        
        # Duplicate nodes beside the original i.e A -> B -> None becomes A -> A copy -> B -> B copy -> null
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next
        
        current = head
        
        
        
        # Assign the random for copied nodes. Since the copied nodes is beside the original,
        # copies of random will be beside the original random
        # Unable to split original and copies at the same time as it is possible for the random
        # to be a previous node
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        current = head
        copyHead = current.next
        prevCopy = Node(0)
        # Split original from copy
        while current:
            prevCopy.next = current.next
            current.next = current.next.next
            current = current.next
            prevCopy = prevCopy.next
        
        return copyHead
            
        
        
        