class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        flag = False
        record_l = [[0]*n for i in range(m)]
        print(record_l)
        
        def search(word_idx, i,j, record_l): 
            
            if word_idx == word_len-1: 
                return True
            left_result, right_result, up_result, down_result = False, False, False, False
            if i + 1 < m and board[i+1][j] == word[word_idx+1] and record_l[i+1][j] !=1:
                record_l[i+1][j] = 1
                up_result = search(word_idx+1, i+1,j, record_l)
                record_l[i+1][j] = 0
            if i - 1 >= 0 and board[i-1][j] == word[word_idx+1] and record_l[i-1][j] !=1 :
                record_l[i-1][j] = 1
                down_result = search(word_idx+1, i-1,j, record_l)
                record_l[i-1][j] = 0
            if j + 1 < n and board[i][j+1] == word[word_idx+1] and record_l[i][j+1] !=1: 
                record_l[i][j+1] =1 
                right_result = search(word_idx+1, i, j+1, record_l)
                record_l[i][j+1] =0
            if j - 1 >= 0 and board[i][j-1] == word[word_idx+1] and record_l[i][j-1] !=1: 
                record_l[i][j-1] =1 
                left_result  = search(word_idx+1, i, j-1, record_l)
                record_l[i][j-1] =0 
            
            return left_result or right_result or down_result or up_result
        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]:
                    record_l[i][j] = 1
                    flag = search(0,i,j, record_l)
                    record_l[i][j] = 0 
                    
                    if flag == True: 
                        return True
        
        return False