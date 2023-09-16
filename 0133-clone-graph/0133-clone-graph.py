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
        visited = {} 
        
        if node == None: 
            return node 
        
        visited[node] = Node(node.val)
        
        dq = deque([node])
        
        while dq: 
            tmp_node = dq.popleft() 
            
            for neigh in tmp_node.neighbors: 
                if neigh not in visited: 
                    visited[neigh] = Node(neigh.val)
                    dq.append(neigh)
                visited[tmp_node].neighbors.append(visited[neigh])
        
        return visited[node]
                    
            
            
            
        
            
        
            
        
        
        