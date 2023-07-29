class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        record_path = [ [0]*n for i in range(m)]
        
        for i in range(m): 
            for j in range(n): 
                
                if i == 0 and j == 0: 
                    record_path[0][0] = 1 
                else: 
                    tmp_cnt = 0 
                    if i-1 >= 0 : 
                        tmp_cnt += record_path[i-1][j]
                    if j-1 >= 0:
                        tmp_cnt += record_path[i][j-1]
    
                    record_path[i][j] = tmp_cnt 
        
        
        return record_path[m-1][n-1]