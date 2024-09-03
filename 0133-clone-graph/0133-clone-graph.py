"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q = deque([])
        nodes = {}
        
        newNode = Node(node.val, [])
        
        q.append(node)
        nodes[node.val] = newNode
        visited = set()
        
        while q:
            node = q.popleft()
            
            if not node or node.val in visited:
                continue

            for neighbor in node.neighbors:
                # Create new copies of node's neighbours if not created already
                if neighbor.val not in nodes:
                    newNeighbor = Node(neighbor.val, [])
                    nodes[neighbor.val] = newNeighbor
                nodes[node.val].neighbors.append(nodes[neighbor.val])
                q.append(neighbor)
            
            visited.add(node.val)
        
        return newNode