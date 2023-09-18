class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: 
            return False
        
        edge_dict = {} 
        connected = set() 
        
        for edge in edges: 
            if edge[0] in edge_dict: 
                edge_dict[edge[0]].append(edge[1])
            else: 
                edge_dict[edge[0]] = [edge[1]]
            
            if edge[1] in edge_dict: 
                edge_dict[edge[1]].append(edge[0])
            else: 
                edge_dict[edge[1]] = [edge[0]]
        
        visited = set() 
        
        def dfs(node, parent): 
            if node in visited:
                return 
            visited.add(node)
            if node in edge_dict: 
                for neighbor in edge_dict[node]: 
                    if parent == neighbor: 
                        continue 
                    if neighbor in visited:
                        return False
                    result = dfs(neighbor, node)
                    if not result: 
                        return False 
                
            return True 
        
    
        
        return dfs(0,-1) and len(visited) == n 
