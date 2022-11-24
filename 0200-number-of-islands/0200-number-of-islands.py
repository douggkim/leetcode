class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        result = [["0"]*m for i in range(n)] 
        cnt = 0 
        
        def bfs(i:int, j:int, grid:List[List[str]], result:List[List[str]])-> List[List[str]]:
            result[i][j] = '1' 
            ip1 = i+1 
            jp1 = j+1 
            im1 = i-1
            jm1 = j-1 
            if ip1< len(grid) and grid[ip1][j] == '1' and result[ip1][j] == '0': 
                # print(f"{i} / {j} triggered")
                result = bfs(ip1,j,grid,result)
            if jp1< len(grid[0]) and grid[i][jp1] == '1' and result[i][jp1] == '0': 
                # print(f"{i} / {j} triggered")
                result = bfs(i,jp1,grid,result)
            if im1 >= 0 and grid[im1][j]=='1' and result[im1][j] == '0':
                # print(f"{i} / {j} triggered")
                result = bfs(im1,j,grid,result)
            if jm1 >= 0 and grid[i][jm1]=='1' and result[i][jm1] == '0':
                # print(f"{i} / {j} triggered")
                result = bfs(i,jm1,grid,result)
            
            return result
        
        for i in range(n):
            for j in range(m): 
                if grid[i][j] == '1' and result[i][j]=='0':
                    # print(f"dfs triggererd cnt: {cnt+1}")
                    cnt += 1 
                    result = bfs(i,j,grid,result)
                    # print(result)
                result[i][j] = '1'
        
        
        return cnt
            
            
                    
            
            