class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        area = 0 
        m = len(grid)
        n = len(grid[0])
        
        record_l = [[0 for i in range(n)] for j in range(m)] 
        
        def explore(i:int, j:int, area:int): 
            record_l[i][j] = 1 
            area += 1 
            move = [[-1,0],[1,0],[0,1],[0,-1]]
            
            for mov in move: 
                new_i = i + mov[0]
                new_j = j + mov[1]
                
                if new_i >= 0 and new_i <m and new_j >=0 and new_j <n and record_l[new_i][new_j] != 1 and grid[new_i][new_j] == 1: 
                    area += explore(new_i,new_j, 0)
            
            return area
        
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1 and record_l[i][j]!=1: 
                    record_l[i][j] = 1 
                    area = explore(i,j,0)
                    max_area = max(area, max_area)
        
        return max_area