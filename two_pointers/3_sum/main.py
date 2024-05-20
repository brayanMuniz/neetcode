# Sort the array, use 2 pointers to find sum, if there is any
# increment first by 1
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
        return result

x = Solution()
print('try 1')
print(x.threeSum([-1,0,1,2,-1,-4]))
print("try 2")
print(x.threeSum([-1,0,1]))
nums3 = [0,0,0]
print("try 3")
print(x.threeSum(nums3))