class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        S= sum([x for x in nums if x%2==0])
        result_list =[]
        for q in queries: 
            if nums[q[1]] %2 ==0 : 
                if q[0] % 2 ==0:
                    S+=q[0]
                    print(S)
                else: 
                    S-=nums[q[1]]
                nums[q[1]]+=q[0]                     
            else: 
                if (nums[q[1]]+q[0]) % 2 ==0:
                    nums[q[1]]+=q[0]
                    S+=nums[q[1]]
                    print(S)
                else: 
                    nums[q[1]]+=q[0]
            result_list.append(S)
        return result_list