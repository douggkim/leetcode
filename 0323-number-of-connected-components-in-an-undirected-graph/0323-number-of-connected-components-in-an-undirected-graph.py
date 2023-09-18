class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_dict = {} 
        
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
        
        def dfs(node, visited) : 
            if node in visited:
                return 
            visited.add(node)
            
            if node in edge_dict: 
                neighbors = edge_dict[node]
                for neighbor in neighbors: 
                    dfs(neighbor, visited)
                
        cnt = 0 
        
        for i in range(n): 
            if i not in visited: 
                dfs(i, visited)
                cnt += 1 
            
        return cnt