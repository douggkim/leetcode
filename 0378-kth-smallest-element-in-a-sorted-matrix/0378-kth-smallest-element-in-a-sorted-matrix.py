class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result_dict = defaultdict(int)
        key_set = set() 
        zero = 0 
        cnt = 0
        for i in range(len(matrix)): 
            for j in range(len(matrix)): 
                if matrix[i][j] == 0: 
                    result_dict[matrix[i][j]] +=1 
                    zero = 1 
                    continue 
                else: 
                    result_dict[matrix[i][j]] +=1 
                    key_set.add(matrix[i][j])
                    
        key_set = sorted(key_set)
        if zero :
            key_set = list(key_set)
            key_set.append(0)
            key_set.sort() 
        
        for i in key_set: 
            cnt += result_dict[i]
            if cnt >= k: 
                return i
                    
            