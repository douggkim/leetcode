class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result_list = []
        S = sum(x for x in nums if x%2 ==0)
        for query in queries: 
            if nums[query[1]] % 2==0: 
                temp = nums[query[1]]
                nums[query[1]] += query[0]
                if nums[query[1]] %2==0:
                    S+= query[0]
                else: 
                    S-= temp
            else:
                nums[query[1]] += query[0]
                if nums[query[1]] %2==0:
                    S+= nums[query[1]]
            result_list.append(S)
        
        return result_list
                    