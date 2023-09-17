class Solution: 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = {}
        
        for preq in prerequisites:
            if preq[0] in course_dict: 
                course_dict[preq[0]].append(preq[1])
            else: 
                course_dict[preq[0]] = [preq[1]]
        
        visited = set() 

        def dfs(course, curr_visit): 
            if course in curr_visit: 
                return True
            if course in visited: 
                return False
            
            curr_visit.add(course)
            if course in course_dict: 
                preqs = course_dict[course]

                for preq in preqs: 
                    is_cycle = dfs(preq, curr_visit)
                    if is_cycle: 
                        return True
                    
            curr_visit.remove(course)
                

            visited.add(course)
            return False 

        for course in course_dict.keys(): 
            is_cycle = dfs(course, set())
            if is_cycle: 
                return False
        
        return True