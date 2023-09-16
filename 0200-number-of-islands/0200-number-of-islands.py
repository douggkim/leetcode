class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        record_l = [[0 for i in range(n)] for j in range(m)]
        cnt = 0 
        
        def traverse(i:int, j:int): 
            move = [[-1,0],[0,-1],[1,0],[0,1]]
            
            for _ in move: 
                
                new_i = i+_[0]
                new_j = j +_[1] 
                if (new_i< m and 0 <= new_i) and (new_j<n and 0<=new_j) and grid[new_i][new_j] == "1" and record_l[new_i][new_j] != 1: 
                    record_l[new_i][new_j] = 1 
                    traverse(new_i, new_j)
        
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] != "0" and record_l[i][j] != 1: 
                    cnt += 1 
                    traverse(i,j)
                    
                    
        
        return cnt
                    