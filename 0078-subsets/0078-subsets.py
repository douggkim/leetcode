class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            # Add the current subset to the result
            result.append(current[:])

            # Explore all possible next elements in the subset
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        result = []
        backtrack(0, [])

        return result
