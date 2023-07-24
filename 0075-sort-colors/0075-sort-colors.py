class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0 for i in range(3)] 

        for i in nums: 
            bucket[i] += 1 
        
        i = 0 
        for j in range(len(bucket)):
            b = bucket[j]
            while b > 0: 
                nums[i] = j 
                b -= 1 
                i += 1

    
                

