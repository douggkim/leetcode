class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        record_l = [[0 for i in range(n+1)] for j in range(m+1)] 
        
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                if text1[i-1] == text2[j-1]: 
                    record_l[i][j] = record_l[i-1][j-1] + 1
                else: 
                    record_l[i][j] = max(record_l[i-1][j], record_l[i][j-1])
        
        return record_l[m][n]
