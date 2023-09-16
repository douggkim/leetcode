"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self): 
        self.visited = {} 
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: 
            return node
        
        if node in self.visited: 
            return self.visited[node]
        
        else: 
            copy_node = Node(node.val)
            self.visited[node] = copy_node 
        
        
        if len(node.neighbors) != 0: 
            copy_node.neighbors = [self.cloneGraph(i) for i in node.neighbors] 
        
        return copy_node
                
                
            
            
            
        
            
        
            
        
        
        