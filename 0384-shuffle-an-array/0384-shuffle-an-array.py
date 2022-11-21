import random 

class Solution:

    def __init__(self, nums: List[int]):
        self.curr = nums 
        self.orig = nums.copy()

    def reset(self) -> List[int]:
        return self.orig 

    def shuffle(self) -> List[int]:
        n = len(self.curr)
        for i in range(n): 
            new_i = random.randint(0,len(self.orig)-1)
            self.curr[new_i], self.curr[i] = self.curr[i], self.curr[new_i]
        
        return self.curr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()