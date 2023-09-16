class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # record minutes
        m = len(grid)
        n = len(grid[0])
        
        record_l = [[0 for j in range(n)] for i in range(m)] 
        
        def dfs(i:int, j:int, min:int): 
            record_l[i][j] = min
            
            move = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for mov in move: 
                new_i = i+mov[0]
                new_j = j+mov[1]
                
                if new_i <0 or new_i >=m or new_j <0 or new_j >=n: 
                    continue 
                
                if record_l[new_i][new_j] > 0 and record_l[new_i][new_j]<=min+1:
                    continue
                
                if grid[new_i][new_j] == 1: 
                    dfs(new_i, new_j, min+1)
        
        # if there is still a fresh orange 
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 2: 
                    move = [[0,1],[0,-1],[1,0],[-1,0]]
                    for mov in move: 
                        new_i = i+mov[0]
                        new_j = j+mov[1]
                        if new_i <0 or new_i >=m or new_j <0 or new_j >=n: 
                            continue
                        if grid[new_i][new_j] == 1 and (record_l[new_i][new_j] == 0 or record_l[new_i][new_j] >1): 
                            dfs(new_i,new_j,1)
        
        max_val = 0 
        
        for i in range(m):
            for j in range(n): 
                if grid[i][j]==1 and record_l[i][j]==0: 
                    return -1
                if grid[i][j]==1 and record_l[i][j] != 0: 
                    max_val = max(record_l[i][j],max_val)
        
        return max_val
                
        