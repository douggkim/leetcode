class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # EC 1 : if nums2 = [] or nums1=[] 
        if len(nums2)==0: 
            return nums1 
        # EC 2: if nums1 only consists of 0 
        if m==0: 
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
            return nums1
        # turn 0 to 1000000001
        for i in range(m,len(nums1)):
            nums1[i] = 1000000001 
        
        # cursors for nums1,2 p_1 and p_2 
        p_1 = p_2 = 0 
        # while p_2 <= len(nums2)-1
        while p_2 <= len(nums2)-1: 
            if nums2[p_2]<=nums1[p_1]: 
                for i in range(len(nums1)-2,p_1-1,-1):
                    nums1[i+1] = nums1[i]
                nums1[p_1]=nums2[p_2]
                p_2+=1
                p_1+=1
            else: 
                p_1+=1
        
        return nums1 
                
        # if p_1 < p_2 <p_1+1 add
        # p_1+1 len(nums)-1  move +1 
        # p_1+1 = nums[p_2] 
        # p_1  stays same 
        # p_2 +=1
        # else : p_1+=1 
        
        