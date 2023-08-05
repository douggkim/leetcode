class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp_stack = [] 
        result_l = [0]*len(temperatures)
        
        for i, temp in enumerate(temperatures): 
            if len(tmp_stack) == 0: 
                tmp_stack.append([i, temp])
            else: 
                while len(tmp_stack) > 0: 
                    if tmp_stack[-1][1] < temp:
                        popped_temp = tmp_stack.pop()
                        popped_idx = popped_temp[0]
                        result_l[popped_idx] = i-popped_idx
                    else:
                        break
                tmp_stack.append([i,temp])
                        
        return result_l 
                        
                