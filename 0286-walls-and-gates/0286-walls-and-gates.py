class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31-1 
        m = len(rooms)
        n = len(rooms[0])
        
        def dfs(i, j, dist): 
            rooms[i][j] = dist 
            move = [[-1,0],[1,0],[0,1],[0,-1]]
            
            for mov in move: 
                new_i = i+mov[0]
                new_j = j+mov[1]
                
                if new_i < 0 or new_i >=m or new_j <0 or new_j >=n: 
                    continue 
                
                if rooms[new_i][new_j] == -1 or rooms[new_i][new_j] == 0: 
                    continue
                
                if rooms[new_i][new_j] > dist+1: 
                    dfs(new_i,new_j, dist+1)
        
        for i in range(m): 
            for j in range(n): 
                if rooms[i][j] == 0: 
                    move = [[-1,0],[1,0],[0,1],[0,-1]]
                    
                    for mov in move: 
                        new_i = i+mov[0]
                        new_j = j+mov[1]

                        if new_i < 0 or new_i >=m or new_j <0 or new_j >=n: 
                            continue 

                        if rooms[new_i][new_j] == -1 or rooms[new_i][new_j] == 0: 
                            continue

                        if rooms[new_i][new_j] > 1: 
                            dfs(new_i,new_j, 1)
        
        
                    