class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        record_l = [[0 for j in range(n)] for i in range(m)] 
        # mark edges 
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'E'
            if board[i][n-1] =='O':
                board[i][n-1] = 'E'
        for j in range(n): 
            if board[0][j] == 'O': 
                board[0][j] = 'E'
            if board[m-1][j] == 'O': 
                board[m-1][j] = 'E'
        
        
        # build a dfs 
        def dfs(i, j, flip_l): 
            global_e_flip_yn = 0 
            flip_l.append((i,j))
            move = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for mov in move: 
                new_i = i+mov[0]
                new_j = j+mov[1]
                
                if new_i < 0 or new_i >=m or new_j < 0 or new_j>=n: 
                    continue
                    
                if board[new_i][new_j] == 'E': 
                    e_flip_yn = 1 
                    return flip_l, e_flip_yn 
                
                if record_l[new_i][new_j] == 1: 
                    continue
                
                
                elif board[new_i][new_j] == 'O': 
                    record_l[new_i][new_j] = 1 
                    flip_l, e_flip_yn = dfs(new_i,new_j, flip_l)
                    global_e_flip_yn = e_flip_yn or global_e_flip_yn
            
            return flip_l, global_e_flip_yn 
        
        for i in range(m): 
            for j in range(n): 
                if record_l[i][j] == 1:
                    continue 
                if board[i][j] == 'O': 
                    
                    flip_l, e_flip_yn = dfs(i,j,[])
                    
                    if e_flip_yn == 1: 
                        replace_val = 'E'
                    else: 
                        replace_val = 'X'
                    
            
                    for tup in flip_l: 
                        board[tup[0]][tup[1]] = replace_val
        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == 'E': 
                    board[i][j] = 'O'
        
        return board
        