from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subset, idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            # Route that has all subsets that include nums[idx]
            subset.append(nums[idx])
            backtrack(subset, idx +1)
            subset.pop()

            # All subsets that dont include nums[idx]
            while idx + 1 < len(nums) and nums[idx] == nums[idx +1]:
                idx += 1

            backtrack(idx +1, subset)

        backtrack([], 0)
        return res
        
