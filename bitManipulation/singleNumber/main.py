from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
        
x = Solution()
print(x.singleNumber([2,2,1]))
