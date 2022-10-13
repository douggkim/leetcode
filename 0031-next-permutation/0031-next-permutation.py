class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2,-1,-1):
            print(i)
            if nums[i+1]>nums[i]:
                min=100000
                for j in range(i,len(nums)): 
                    if nums[j]>nums[i]:
                        if min>nums[j]:
                            min = nums[j]
                            min_idx = j
                print(f"min {min}")
                nums[min_idx] = nums[i]
                nums[i] = min
                nums[i+1:] = sorted(nums[i+1:])

                break
            if i==0 :
                nums.sort()
                break
            