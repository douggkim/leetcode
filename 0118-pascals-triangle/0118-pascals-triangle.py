class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        
        memo = []
        # check if numRows-1 in memo 
        # if not
        for i in range(numRows):
            new_row = [None]*(i+1)
            new_row[0] = 1
            new_row[i] = 1
            for j in range(1,i):  
                new_row[j]=memo[i-1][j-1]+memo[i-1][j]
            memo.append(new_row)
        return memo
        # for i in range(len(numRows))
        # new_row = []
        # for j in range(numRows-1)
        # 0 = 1 / numRows-1 = 1 
        # else : numRows[i-1][j-1] + numRows[j]
        
        
        