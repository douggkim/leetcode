class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.searchRow(matrix, target)
    
    # Get a function to find the row where  - binary search 
    # row[i][0] <= target <= row[i+1][0]
    def searchRow(self, matrix:List[List[int]], target:int) -> bool: 
        numRows = len(matrix) -1
        numCols = len(matrix[0])-1 
        rowStart = 0 
        rowEnd = numRows
        currentRow = (rowStart+rowEnd)//2 
        prevRow = math.inf


        while currentRow >= 0 and currentRow <=numRows and prevRow != currentRow: 
            prevRow = currentRow
            if matrix[currentRow][0] <= target and target <= matrix[currentRow][numCols]: 
                return self.searchCol(matrix, currentRow, target)
            elif target < matrix[currentRow][numCols]:
                rowEnd = currentRow-1 
                currentRow = (rowStart+rowEnd)//2 
            else: 
                rowStart = currentRow+1
                currentRow = (rowStart+rowEnd)//2 
        
        return False 

            

    # Get a function to find the column where - binary search 
    # row[i][j] <= target <= row[i+1][j+1]
    def searchCol(self,matrix:List[List[int]], currentRow:int, target:int) -> bool: 
        numCols = len(matrix[currentRow])-1
        colStart = 0 
        colEnd = numCols
        currentCol = (colStart+colEnd)//2

        target_row = matrix[currentRow]
        prevCol = math.inf

        while currentCol >= 0 and currentCol <= numCols and prevCol != currentCol:
            prevCol = currentCol 
            if target_row[currentCol] == target: 
                return True
            elif target < target_row[currentCol]:
                colEnd = currentCol -1 
                currentCol = (colStart +colEnd)//2 
            else: 
                colStart = currentCol + 1 
                currentCol = (colStart+colEnd)//2 
        return False 


    # If none