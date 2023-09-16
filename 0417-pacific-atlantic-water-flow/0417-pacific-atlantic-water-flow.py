class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or len(heights)==0: 
            return [] 
        m = len(heights)
        n = len(heights[0])
        
        def dfs(i:int, j:int, reach): 
            reach.add((i,j))
            move = [[-1,0],[1,0],[0,-1],[0,1]]
            
            for mov in move: 
                new_i = i+mov[0]
                new_j = j+mov[1]
                
                if (new_i,new_j) in reach:
                    continue 
                
                if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                    continue
                
                if heights[new_i][new_j] < heights[i][j]: 
                    continue 
                    
                reach = dfs(new_i,new_j, reach)
                
            return reach
        
        atl_reach = set() 
        pac_reach = set() 
        for i in range(m): 
            pac_reach = dfs(i,0,pac_reach)
            atl_reach = dfs(i,n-1, atl_reach)
        for j in range(n): 
            pac_reach = dfs(0,j, pac_reach)
            atl_reach = dfs(m-1,j,atl_reach)
        
        return list(pac_reach.intersection(atl_reach))
            