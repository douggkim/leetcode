class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board: 
            check_set = set()
            for num in row: 
                if num in check_set: 
                    return False 
                elif num != '.': 
                    check_set.add(num)
        
        col_idx = 0 
        while col_idx <= 8: 
            check_set = set() 
            for row in board: 
                if row[col_idx] in check_set: 
                    return False 
                elif row[col_idx] != '.': 
                    check_set.add(row[col_idx])
            col_idx += 1 
        
        
        for start_row_idx in range(0,9,3): 
            for start_col_idx in range(0,9,3): 
                check_set = set() 
                for r_idx in range(start_row_idx, start_row_idx+3): 
                    for c_idx in range(start_col_idx, start_col_idx+3): 
                        if board[r_idx][c_idx] in check_set: 
                            return False 
                        elif board[r_idx][c_idx] != '.': 
                            check_set.add(board[r_idx][c_idx])
        
        return True 
                
#         each row
        
    
    

#  each column 

#  each square 
        