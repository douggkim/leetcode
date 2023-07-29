class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        record_path = [[0]*n for i in range(m)]
    
        for i in range(m):
            for j in range(n): 
                if obstacleGrid[i][j] == 1: 
                    continue 
                elif i == 0 and j == 0 : 
                    record_path[i][j] = 1
                else: 
                    tmp_cnt = 0 
                    if i-1 >= 0: 
                        tmp_cnt += record_path[i-1][j]
                    if j-1 >= 0: 
                        tmp_cnt += record_path[i][j-1]
                    
                    record_path[i][j] = tmp_cnt 
        
        return record_path[m-1][n-1]
                        