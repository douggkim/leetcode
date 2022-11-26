class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate_updown(matrix) : 
            n = len(matrix)
            m = len(matrix[0])
            for i in range((n//2)): 
                for j in range(m): 
                    matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
        def rotate_cross(matrix): 
            n = len(matrix) 
            m = len(matrix[0])
            for i in range(n):
                for j in range(i+1):
                    matrix[i][j],matrix[j][i] =matrix[j][i],matrix[i][j]  
                    
        rotate_updown(matrix)
        rotate_cross(matrix)
        
        return matrix
                    
        