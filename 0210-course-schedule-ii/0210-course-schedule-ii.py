class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_dict = {}
        
        for preq in prerequisites: 
            if preq[0] in preq_dict: 
                preq_dict[preq[0]].append(preq[1])
            else: 
                preq_dict[preq[0]] = [preq[1]] 
                
        visited = set() 
        visited_l = [] 
        def search_cycle(course, curr_visit): 
            if course in curr_visit: 
                return True 
            
            if course in visited: 
                return False 
            
            curr_visit.add(course)
            if course in preq_dict: 
                preqs = preq_dict[course]
                
                for preq in preqs: 
                    is_cycle = search_cycle(preq, curr_visit)
                    if is_cycle:
                        return True
            curr_visit.remove(course)
            visited.add(course)
            if course not in set(visited_l): 
                visited_l.append(course)
            
            
            return False 
        
        for course in range(numCourses): 
            if course in preq_dict: 
                is_cycle = search_cycle(course, set())
                if is_cycle: 
                    return [] 
            elif course not in visited_l: 
                visited_l.append(course)
        
        return visited_l 
            
            
        
        
                    
            
                