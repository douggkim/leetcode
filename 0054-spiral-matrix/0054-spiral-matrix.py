class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = [] 
        def spiral(matrix, start_i, start_j, r ): 
            i= start_i 
            j = start_j 
            m = len(matrix) 
            n = len(matrix[0])
            
            if start_i*2 > m-1 or start_j*2 > n-1: 
                return r 
            
            while j < n-start_i:
                r.append(matrix[i][j])
                # print(matrix[i][j])
                j+=1 
            
            i = start_i + 1 
            j = n-start_i - 1 
            
            while i < m-start_j:
                r.append(matrix[i][j])
                # print(matrix[i][j])
                i+=1 
                
            i = m -start_i -1
            j = n - start_j - 2
            if m-start_i*2>1 and n-start_j*2>1: 
                while j > start_j-1: 
                    r.append(matrix[i][j])
                    j -= 1 

                i = m - start_i - 2 
                j = start_j

                while i > start_i: 
                    r.append(matrix[i][j])
                    i -= 1 

            # print(r)

            r = spiral(matrix, start_i+1, start_j+1,r)
            
            return r 
        
        r = spiral(matrix,0,0,r)
        
        return r 
                
            
            
                
                