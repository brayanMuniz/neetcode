from typing import List

# use a left and right pointer to expand 
# if the prefix of the subarray(left pointer) is negative, skip it
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            maxSub = max(maxSub, currentSum)

        return maxSub
