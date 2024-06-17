from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 3, 4]

        result = [1] * len(nums)
        # [1, 1, 1, 1]

        #prefix : | 1 | a | a * b | a * b * c |
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        # [1, 1, 2, 6]   

        #postfix : |b * c * d |  c * d | d | 1 | 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        # [24, 12, 4, 1] 

        return result


    
x = Solution()
print(x.productExceptSelf([1,2,3,4]))
